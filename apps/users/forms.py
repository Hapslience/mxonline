# -*- coding:utf-8 -*-
__author__ = 'lx'
__date__ = ' 下午4:37'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

