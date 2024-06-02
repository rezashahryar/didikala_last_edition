from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Prefetch

from .models import Product, SetProductProperty
# Create your views here.


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        global product
        slug = self.kwargs.get('slug')
        product = get_object_or_404(
            Product.objects.select_related('sub_category') \
                .select_related('sub_sub_category').prefetch_related(Prefetch(
                    'properties',
                    queryset=SetProductProperty.objects.select_related('property')
                )), 
            slug=slug
        )

        return product
    
    def get_template_names(self):
        if product.available:
            return ['products/product_detail.html']
        else:
            return ['products/product_not_available.html']
