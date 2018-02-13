# -*- encoding:utf-8 -*-
from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from .forms import LoginForm
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username = username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', )

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username = user_name, password = pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'msg':'用户名或者密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


