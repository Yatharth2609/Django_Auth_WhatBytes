"""
URL configuration for authproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_auth import views as auth_views

#All the required Endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.home_view, name='home'),
    path('auth/signup/', auth_views.signup_view, name='signup'),
    path('auth/login/', auth_views.login_view, name='login'),
    path('auth/logout/', auth_views.logout_view, name='logout'),
    path('auth/password_reset/', auth_views.password_reset_view, name='password_reset'),
    path('auth/password_change/', auth_views.password_change_view, name='password_change'),
    path('auth/dashboard/', auth_views.dashboard_view, name='dashboard'),
    path('auth/profile/', auth_views.profile_view, name='profile'),
]
