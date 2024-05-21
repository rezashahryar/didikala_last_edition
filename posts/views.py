from django.views import generic

# Create your views here.

class PostListView(generic.TemplateView):
    template_name = 'posts/post_list.html'