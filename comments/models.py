from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')

    title = models.CharField(max_length=255)
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-datetime_created',)

    def __str__(self):
        return f'{self.user} for {self.post}'
    

class PostCommentScore(models.Model):
    SCORE = [
        ('l', _('like')),
        ('dl', _('dislike')),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like')
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name='scores')
    score = models.CharField(max_length=3, choices=SCORE)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment.title} {self.score}'
