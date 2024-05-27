from django import template
from comments.models import PostCommentScore
from posts.models import Tag, Category, Post

register = template.Library()


@register.inclusion_tag('includes/comment_of_post_scores.html')
def comment_of_product_scores(comment):
    # queryset = ProductCommentScore.objects.filter(comment_id=comment.id).all()
    like_count = PostCommentScore.objects.filter(score='l', comment_id=comment.id).count()
    dislike_count = PostCommentScore.objects.filter(score='dl', comment_id=comment.id).count()
    return {
        "like_count": like_count,
        "dislike_count": dislike_count,
        "comment": comment,
    }


@register.inclusion_tag('includes/list_tag_sidebar_posts_section.html')
def tag_list():
    tags = Tag.objects.all()
    return {
        "tags": tags
    }


@register.inclusion_tag('includes/list_category_sidebar_posts_section.html')
def category_list():
    categories = Category.objects.all()
    return {
        "categories": categories
    }


@register.inclusion_tag('includes/latest_post.html')
def latest_posts():
    posts = Post.published.all()[:4]

    return {
        "latest_posts": posts
    }
