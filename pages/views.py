from django.shortcuts import redirect, render
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib import messages

from products.models import ProductCategory, SubProductCategory, Product

from .forms import UserEmailForm
# Create your views here.

@require_POST
def save_email_users(request):
    form = UserEmailForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'ایمیل شما با موفقیت در سیستم ثبت شد.')
    else:
        print(form.errors)

    return redirect('pages:home')

class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class WelcomePageView(generic.TemplateView):
    template_name = 'pages/welcome_page.html'
