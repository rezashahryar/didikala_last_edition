from django.shortcuts import render
from django.views import generic
# Create your views here.

class ProfileView(generic.TemplateView):
    template_name = 'profiles/profile.html'


def profile_edit_view(request):

    return render(request, 'profiles/profile_edit.html')
