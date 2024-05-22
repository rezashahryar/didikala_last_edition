from django.views import generic
from django.shortcuts import get_object_or_404
from . models import Post, Tag, Category
# Create your views here.

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=True).defer(
                                                    'description',
                                                    'datetime_modified',
                                                    'status',
                                                )
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all().defer(
                                            'datetime_created', 
                                            'datetime_modified',
                                          )
        context['categories'] = Category.objects.all().defer(
                                                        'datetime_created',
                                                        'datetime_modified',
                                                    )

        return context
    

class PostDetailView(generic.DetailView):
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug__exact=slug)
        
        return post