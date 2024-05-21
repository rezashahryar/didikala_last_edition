from django.views import generic
from . models import Post
# Create your views here.

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'