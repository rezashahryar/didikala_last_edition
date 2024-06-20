from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profiles/profile.html'


@login_required
def profile_edit_view(request):

    return render(request, 'profiles/profile_edit.html')
