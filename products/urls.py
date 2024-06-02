from django.urls import path
from . import views

# create your urls here

app_name = 'products'

urlpatterns = [
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
