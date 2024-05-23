from django import template
from comments.models import PostCommentScore

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