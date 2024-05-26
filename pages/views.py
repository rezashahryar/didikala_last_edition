from django.views import generic

# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'


class PageFaqView(generic.TemplateView):
    template_name = 'pages/page_faq.html'


class PageFaqCategoryView(generic.TemplateView):
    template_name = 'pages/page_faq_category.html'


class PageFaqQuestionView(generic.TemplateView):
    template_name = 'pages/page_faq_question.html'


class PagePrivacyView(generic.TemplateView):
    template_name = 'pages/page_privacy.html'
