from django.views import generic
from django.db.models import Prefetch
from products.models import ProductCategory, SubProductCategory
# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all().prefetch_related(Prefetch(
            'children',
            queryset=SubProductCategory.objects.select_related('parent')
        ))
        return context


class PageFaqView(generic.TemplateView):
    template_name = 'pages/page_faq.html'


class PageFaqCategoryView(generic.TemplateView):
    template_name = 'pages/page_faq_category.html'


class PageFaqQuestionView(generic.TemplateView):
    template_name = 'pages/page_faq_question.html'


class PagePrivacyView(generic.TemplateView):
    template_name = 'pages/page_privacy.html'
