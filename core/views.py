from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.views import generic
from .forms import LoginForm
# Create your views here.

class LoginView(generic.FormView):
    http_method_names = ['get', 'post']
    template_name = 'core/login.html'
    form_class = LoginForm
