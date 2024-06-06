from django.urls import path
from . import views

# create your urls here

app_name = 'orders'

urlpatterns = [
    path('', views.order_view, name='order_detail'),
]
