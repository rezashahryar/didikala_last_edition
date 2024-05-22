from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to='posts/')

    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    status = models.BooleanField(default=True)

    datetime_created = jmodels.jDateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-datetime_created',)

    def __str__(self):
        return self.title