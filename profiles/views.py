from django.shortcuts import render

# Create your views here.

def profile(request):

    return render(request, 'profiles/profile.html')


def profile_edit_view(request):

    return render(request, 'profiles/profile_edit.html')
