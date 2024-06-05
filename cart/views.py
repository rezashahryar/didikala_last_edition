from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import generic

from products.models import Product

from .cart import Cart, NextCart

# Create your views here.


class CartDetailView(generic.ListView):
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

    def get_queryset(self):
        global cart
        cart = Cart(self.request)
        return cart
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_cart'] = NextCart(self.request)
        return context
    
    def get_template_names(self):
        if len(self.get_queryset()) == 0:
            return ['cart/cart_empty.html']
        return ['cart/cart_detail.html']


class CartAddItemView(generic.View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')

        cart = Cart(request)
        cart.add(product, quantity, color)

        return redirect('cart:cart_detail')
    

class CartDeleteItemView(generic.View):

    def post(self, request, id):
        cart = Cart(request)
        cart.delete(id)

        return redirect('cart:cart_detail')
    

class CartDeleteItemHomePageView(generic.View):
    
    def post(self, request, id):
        cart = Cart(request)
        cart.delete(id)

        return redirect('pages:home')
    

class AddItemToNextCart(generic.View):

    def post(self, request, id):
        next_cart = NextCart(request)
        item = request.session.get('cart').get(id)
        product = get_object_or_404(Product, pk=item.get('id'))
        next_cart.add(
            product,
            quantity=item.get('quantity'),
            color=item.get('color')
        )
        return HttpResponse("hello")
