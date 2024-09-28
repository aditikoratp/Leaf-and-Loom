"""
URL configuration for Leaf_and_Loom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


from django.urls import path
from . import views
from django.urls import path, include
from django.shortcuts import get_object_or_404

app_name = 'leaf and loom'
from .views import CustomLoginView
from .views import register, login_view

urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.login_view, name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),

    #path('', views.home, name='home'),  # Add your home view if needed
    # ... other URL patterns ...
    #path('user/', views.user_profile_page, name='user_profile_page')
]



