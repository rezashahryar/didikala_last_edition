from django.urls import path
from . import views

# create your urls here

app_name = 'cart'

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>/', views.CartAddItemView.as_view(), name='cart_add_item'),
    path('delete/<str:id>/', views.CartDeleteItemView.as_view(), name='cart_delete_item'), 
    path('delete/home-page/<str:id>/', views.CartDeleteItemHomePageView.as_view(), name='cart_delete_item_home_page'), 
    # path('add/next-cart/<str:id>/', views.AddItemToNextCart.as_view(), name='add_item_to_next_cart'),
]

