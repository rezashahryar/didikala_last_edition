from django.urls import path
from . import views

# create your urls here

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='cart_detail'),
]

