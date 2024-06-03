from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegisterForm
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
            print("valid")
        else:
            print("not valid")
            print(login_form.errors)

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
            new_register_form = register_form.save()
            new_register_form.username = f'user_{new_register_form.pk}'

            if len(cd['username']) == 11 and cd['username'].isdigit():
                new_register_form.mobile = cd['username']
            elif cd['username'].find('@') and cd['username'][-4:] == '.com':
                new_register_form.email = cd['username']
            new_register_form.set_password(cd['password'])
            new_register_form.save()
        else:
            print(register_form.errors)

    context = {
        "register_form": register_form
    }

    return render(request, 'core/register.html', context)


class LogoutView(LoginRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        messages.warning(request, 'با موفقیت از حساب کاربری خود خارج شدید')
        return redirect('pages:home')
