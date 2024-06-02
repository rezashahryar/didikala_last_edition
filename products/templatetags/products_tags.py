from django import template
from comments.models import ProductCommentScore, ProductComment

register = template.Library()


@register.inclusion_tag('includes/comment_of_product_scores.html')
def comment_of_product_scores(comment):
    # queryset = ProductCommentScore.objects.filter(comment_id=comment.id).all()
    like_count = ProductCommentScore.objects.all().filter(score='l', comment_id=comment.id).count()
    dislike_count = ProductCommentScore.objects.filter(score='dl', comment_id=comment.id).count()
    return {
        "like_count": like_count,
        "dislike_count": dislike_count,
        "comment": comment,
    }
