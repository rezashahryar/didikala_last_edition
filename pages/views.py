from django.views import generic
from django.db.models import Prefetch
from products.models import ProductCategory, SubProductCategory, Product
# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all().prefetch_related('children__sub_children')
        context['best_sellers'] = Product.objects.all() \
            .select_related('category').order_by('-sales_number')[:7]
        context['discounted_products'] = Product.objects.filter(discount__gt=0).select_related('category')
        context['most_visited'] = Product.objects.all().order_by('-counted_views').select_related('category')
        return context


class PageFaqView(generic.TemplateView):
    template_name = 'pages/page_faq.html'


class PageFaqCategoryView(generic.TemplateView):
    template_name = 'pages/page_faq_category.html'


class PageFaqQuestionView(generic.TemplateView):
    template_name = 'pages/page_faq_question.html'


class PagePrivacyView(generic.TemplateView):
    template_name = 'pages/page_privacy.html'
