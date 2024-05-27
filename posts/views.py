from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from comments.models import PostComment
from .models import Post, Tag, Category

# Create your views here.


class PostListView(generic.ListView):
    queryset = Post.published.all().defer(
        "description",
        "datetime_modified",
        "status",
    )
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    paginate_by = 1


class PostDetailView(generic.DetailView):
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_object(self):
        slug = self.kwargs.get("slug")
        post = get_object_or_404(
            Post.published.select_related("category") \
            .select_related("author") \
            .prefetch_related(
                Prefetch(
                    "comments", 
                    queryset=PostComment.objects.select_related("user")
                )
            ),
            slug__exact=slug,
        )

        return post


class CategoryObjectView(generic.ListView):
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        cat_slug = self.kwargs.get("slug")
        category = get_object_or_404(Category, slug__exact=cat_slug)

        return category.posts.filter(status=Post.POST_STATUS_PUBLISHED)


class TagObjectView(generic.ListView):
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("slug")
        tag = get_object_or_404(Tag, slug__exact=tag_slug)

        return tag.posts.filter(status=Post.POST_STATUS_PUBLISHED)
