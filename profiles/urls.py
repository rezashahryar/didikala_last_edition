from django.urls import path
from . import views

# create your urls here

app_name = 'profiles'

urlpatterns = [
    path('edit/', views.profile_edit_view, name='profile_edit'),
]
