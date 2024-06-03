from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm
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


class LogoutView(LoginRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        messages.warning(request, 'با موفقیت از حساب کاربری خود خارج شدید')
        return redirect('pages:home')
