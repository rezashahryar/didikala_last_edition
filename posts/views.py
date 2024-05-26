from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from comments.models import PostComment
from . models import Post, Tag, Category
# Create your views here.

class PostListView(generic.ListView):
    queryset = Post.published.all().defer(
                                        'description',
                                        'datetime_modified',
                                        'status',
                                    )
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all().defer(
                                    'datetime_created', 
                                    'datetime_modified',
                                )
        context['tags'] = tags
        categories = Category.objects.all().defer(
                                                'datetime_created',
                                                'datetime_modified',
                                            )
        context['categories'] = categories

        return context
    

class PostDetailView(generic.DetailView):
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        slug = self.kwargs.get('slug')
        post = get_object_or_404(Post.objects.select_related('category').select_related('author').prefetch_related(
                                                            Prefetch(
                                                                'comments',
                                                                queryset=PostComment.objects.select_related('user')                                     
                                                            )), 
                                slug__exact=slug,
                                )
        
        return post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all()[:4]
        context['categories'] = Category.objects.all().defer(
                                                        'datetime_created',
                                                        'datetime_modified',
                                                    )
        context['tags'] = Tag.objects.all().defer(
                                                'datetime_created', 
                                                'datetime_modified',
                                            )

        return context
