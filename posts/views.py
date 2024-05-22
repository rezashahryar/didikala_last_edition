from django.views import generic
from . models import Post, Tag
# Create your views here.

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()

        return context