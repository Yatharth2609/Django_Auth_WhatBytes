from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Function to in take email as well at the time of Registration
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

#Custom Funcion for Changing the UserName after Registration
class UsernameChangeForm(forms.Form):
    new_username = forms.CharField(max_length=150, required=True)

    def clean_new_username(self):
        username = self.cleaned_data.get('new_username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username
