from django.shortcuts import render
from django.views import generic
# Create your views here.


class CartDetailView(generic.TemplateView):
    template_name = 'cart/cart_detail.html'
