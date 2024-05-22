from django.db import models
from django.conf import settings
# Create your models here.


class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')

    title = models.CharField(max_length=255)
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} for {self.post}'
