from django.shortcuts import render, get_object_or_404
from .models import Restaurant

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import F, FloatField
from django.db.models.functions import Sqrt, Power


class CustomLoginView(LoginView):
    template_name = 'login.html'

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, f'Account created for {user.username}!')
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# myapp/views.py

class CustomLoginView(LoginView):
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        else:
            print(form.errors)

    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                # go to settings.py to change redirect behavior after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def user_profile_page(request):  # add user id parameter
    # add logic to check if user is signed in
    # current_user = get_object_or_404(User, pk=user_id)
    return render(request,
                  "foodie/userPage.html")  # return render(request, "foodie/userPage.html", {'user_id' : user_id})


def filter_restaurant(request):
