from django.shortcuts import redirect, get_object_or_404
from django.views import generic

from products.models import Product

from .cart import Cart

# Create your views here.


class CartDetailView(generic.ListView):
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

    def get_queryset(self):
        cart = Cart(self.request)
        return cart


class CartAddItemView(generic.View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')

        cart = Cart(request)
        cart.add(product, quantity, color)

        return redirect('cart:cart_detail')