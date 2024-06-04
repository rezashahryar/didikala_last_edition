from django.urls import path
from . import views

# create your urls here

app_name = 'cart'

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>/', views.CartAddItemView.as_view(), name='cart_add_item')
]

