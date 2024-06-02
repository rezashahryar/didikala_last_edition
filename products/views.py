from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product
# Create your views here.


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

        return product

