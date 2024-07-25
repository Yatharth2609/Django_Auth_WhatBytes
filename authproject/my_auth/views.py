from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponse
from .forms import UsernameChangeForm, CustomUserCreationForm


#This is for User Sign Up Functionality
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'my_auth/signup.html', {'form': form})

#This is for User Login Functionality
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'my_auth/login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            return render(request, 'my_auth/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
        return render(request, 'my_auth/login.html', {'form': form})
    
#This is for User Logout
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

#This is for Password Reset Functionality
def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            send_mail(
                'Password Reset Request',
                'Click the link below to reset your password:',
                'yatharth.mishra2002@gmail.com',
                [user.email],
                fail_silently=False,
            )
        return redirect('login')
    return render(request, 'my_auth/password_reset.html')

#This is for Change Password Functionality
@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'my_auth/password_change.html', {'form': form})

#This is for Dashboard View Functionality
@login_required
def dashboard_view(request):
    return render(request, 'my_auth/dashboard.html')

#This is for Profile View Functionality
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UsernameChangeForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            user = request.user
            user.username = new_username
            user.save()
            return redirect('profile')  # Redirect to profile page to reflect changes
    else:
        form = UsernameChangeForm()

    return render(request, 'my_auth/profile.html', {
        'user': request.user,
        'form': form
    })
