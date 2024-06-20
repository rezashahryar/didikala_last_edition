import random

from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegisterForm
from .models import ActivationViaEmail, User
from .send_mail import send_activation_email
# Create your views here.

def login_view(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            if cd['remember_me']:
                request.session.set_expiry(604800)
            else:
                request.session.set_expiry(0)
            
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                print('useruser')
                if next_page:
                    return redirect(next_page)
                return redirect('pages:home')

    context = {
        "login_form": login_form,
    }

    return render(request, 'core/login.html', context)


def register_view(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            # new_register_form = register_form.save()
            # new_register_form.username = f'user_{new_register_form.pk}'

            if len(cd['username']) == 11 and cd['username'].isdigit():

                request.session['username'] = cd.get('username')

            elif cd['username'].find('@') and cd['username'][-4:] == '.com':

                request.session['username'] = cd.get('username')
                request.session['password'] = cd.get('password')

                # send email
                code = random.randint(10000, 99999)
                act = ActivationViaEmail(
                    code=code,
                    email=cd.get('username')
                )
                act.save()
                print('email*' * 40)
                print(cd.get('username'))
                send_activation_email(request, cd.get('username'), code)

            # new_register_form.set_password(cd['password'])
            # new_register_form.save()

            return redirect('core:activate')
        else:
            print(register_form.errors)
            print('not valid')

    context = {
        "register_form": register_form
    }

    return render(request, 'core/register.html', context)


class VerifyCodeView(generic.View):

    def get(self, request):
        return render(request, 'core/verify_code.html')
    
    def post(self, request):
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        num4 = request.POST.get('num4')
        num5 = request.POST.get('num5')

        code = f'{num1}{num2}{num3}{num4}{num5}'

        username = request.session.get('username')
        password = request.session.get('password')

        if code is not None:
            user = User()

            if len(username) == 11 and username.isdigit():
                user.mobile = username

            elif username.find('@') and username[-4:] == '.com':
                user.email = username

            user.set_password(password)
            user.save()
            user.username = f'user_{user.pk}'
            user.save()
            
        return redirect('pages:welcome_page')


class LogoutView(LoginRequiredMixin, generic.View):

    def get(self, request):
        logout(request)
        messages.warning(request, 'با موفقیت از حساب کاربری خود خارج شدید')
        return redirect('pages:home')
