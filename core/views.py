from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string

from .forms import LoginForm, RegisterForm
from .models import ActivationViaEmail
from.send_mail import send_activation_email
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
                new_register_form.is_active = False
                new_register_form.email = cd['username']

                # send email
                code = get_random_string(20)
                act = ActivationViaEmail(
                    code=code,
                    user=new_register_form
                )
                act.save()
                send_activation_email(request, new_register_form.email, code)

            new_register_form.set_password(cd['password'])
            new_register_form.save()

            return redirect('core:login')
        else:
            # print(register_form.errors)
            print('not valid')

    context = {
        "register_form": register_form
    }

    return render(request, 'core/register.html', context)



class ActivateView(generic.View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(ActivationViaEmail, code=code)

        # Activate profile
        user = act.user
        user.is_active = True
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, 'فعالسازی اکانت شما با موفقیت انجام شد.')

        return redirect('core:login')


class LogoutView(LoginRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        messages.warning(request, 'با موفقیت از حساب کاربری خود خارج شدید')
        return redirect('pages:home')
