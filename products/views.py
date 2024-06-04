from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.views import generic
from django.db.models import Prefetch
from django.views.decorators.http import require_POST

from comments.models import ProductComment, ProductPoints

from .models import Product, ProductCategory, SetProductProperty, Question, SubProductCategory, SubSubProductCategory
from .forms import QuestionForm

# Create your views here.

class ProductsOfCategoryListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        global category_object
        category_slug = self.kwargs.get('cat_slug')
        category_object = get_object_or_404(ProductCategory, slug=category_slug)

        products = get_list_or_404(Product, category=category_object)

        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category_object

        return context
    

class ProductOfSubCategoryListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        sub_cat = self.kwargs.get('sub_category')
        sub_category_object = get_object_or_404(SubProductCategory, slug=sub_cat)

        products = get_list_or_404(Product, sub_category=sub_category_object)

        return products


class ProductOfSubSubCategoryListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        sub_sub_cat_slug = self.kwargs.get('sub_sub_category')
        sub_sub_category_obj = get_object_or_404(SubSubProductCategory, slug=sub_sub_cat_slug)

        products = get_list_or_404(Product, sub_sub_category=sub_sub_category_obj)

        return products


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        global product
        global slug
        slug = self.kwargs.get('slug')
        product = get_object_or_404(
            Product.objects.select_related('sub_category') \
                .select_related('sub_sub_category').prefetch_related(Prefetch(
                    'properties',
                    queryset=SetProductProperty.objects.select_related('property')
                )).prefetch_related(Prefetch(
                    'questions',
                    queryset=Question.objects.select_related('user').select_related('parent').prefetch_related('answers__user')
                )).prefetch_related(Prefetch(
                    'comments',                      
                    queryset=ProductComment.approved.select_related('product').select_related('user').prefetch_related(Prefetch(
                        'product_points',
                        queryset=ProductPoints.objects.prefetch_related('good_point').prefetch_related('weak_point')
                    ))
                )), 
            slug=slug
        )

        return product
    
    def get_template_names(self):
        if product.available or product.inventory > 0:
            return ['products/product_detail.html']
        else:
            return ['products/product_not_available.html']
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comments'] = ProductComment.approved.filter(product__slug=slug).prefetch_related('product_points').select_related('product').select_related('user')
        return context
    

@require_POST
def question(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.product = product
            new_form.save()
            return redirect('products:product_detail', product.slug)


@require_POST
def answer(request, pk, qpk):
    product = get_object_or_404(Product, pk=pk)
    question_id = get_object_or_404(Question, pk=qpk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.product = product
            new_form.parent = question_id
            new_form.save()
            return redirect('products:product_detail', product.slug)
