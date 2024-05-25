from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class PostManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.POST_STATUS_PUBLISHED)


class Post(models.Model):
    POST_STATUS_PUBLISHED = 'p'
    POST_STATUS_DRAFT = 'd'

    POST_STATUS = (
        (POST_STATUS_PUBLISHED, 'Published'),
        (POST_STATUS_DRAFT, 'Draft')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    cover = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    status = models.CharField(max_length=2, choices=POST_STATUS, default=POST_STATUS_PUBLISHED)

    datetime_created = jmodels.jDateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PostManager()

    class Meta:
        db_table = 'post'
        ordering = ('-datetime_created',)

    def __str__(self):
        return self.title