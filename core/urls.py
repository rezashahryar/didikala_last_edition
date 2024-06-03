from django.urls import path
from . import views

# create your urls here

app_name = 'core'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
