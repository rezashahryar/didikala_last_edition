from django.views import generic

# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'pages/home.html'