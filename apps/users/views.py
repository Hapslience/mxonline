# -*- encoding:utf-8 -*-
from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.views.generic import View
from django.contrib.auth.backends import ModelBackend
from .forms import LoginForm, RegisterForm
from django.db.models import Q
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email = username))
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


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', )

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(Q(email=email) | Q(username=email)):
                return render(request, 'register.html', {'msg':'用户已经存在了'})
            else:
                password = request.POST.get('password', '')
                user_profile = UserProfile()
                user_profile.email = email
                user_profile.password = make_password(password)
                user_profile.username = email
                user_profile.save()
                return render(request, 'index.html', {})

            return render(request, 'register.html', {'msg': '账号或者密码不符合规则'})
        return render(request, 'register.html', {'register_form':register_form})


