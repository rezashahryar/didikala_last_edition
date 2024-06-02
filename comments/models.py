from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from products.models import Product
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


class GoodPoint(models.Model):
    good_point = models.CharField(_('ویژگی خوب'), max_length=255)


class WeakPoint(models.Model):
    weak_point = models.CharField(_('ویژگی بد'), max_length=255)


class ProductPoints(models.Model):
    comment = models.ForeignKey('ProductComment', on_delete=models.CASCADE, related_name='product_points', verbose_name=_('کامنت'))
    good_point = models.ManyToManyField(GoodPoint, related_name='good_points', verbose_name=_('ویژگی های خوب'))
    weak_point = models.ManyToManyField(WeakPoint, related_name='weak_points', verbose_name=_('ویژگی های بد'))


class ProductCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(comment_status=ProductComment.COMMENT_STATUS_APPROVED)


class ProductComment(models.Model):
    COMMENT_STATUS_WAITING = 'w'
    COMMENT_STATUS_APPROVED = 'a'
    COMMENT_STATUS_NOT_APPROVED = 'na'
    COMMENT_STATUS = [
        (COMMENT_STATUS_WAITING, 'Waiting'),
        (COMMENT_STATUS_APPROVED, 'Approved'),
        (COMMENT_STATUS_NOT_APPROVED, 'Not Approved')
    ]

    I_DONT_SUGGEST = 'i_d_s'
    I_SUGGEST = 'i_s'
    NO_IDEA = 'n_i'
    SUGGEST_BUY_PRODUCT = [
        (I_SUGGEST, _('پیشنهاد میکنم')),
        (I_DONT_SUGGEST, _('خیر پیشنهاد نمی کنم')),
        (NO_IDEA, _('نظری ندارم'))
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='user_comments' ,verbose_name=_('کاربر'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('محصول'))
    title = models.CharField(_('عنوان'), max_length=300)

    text = models.TextField(_('متن'))
    suggest_buy_product = models.CharField(_('پیشنهاد برای خرید'), max_length=20, choices=SUGGEST_BUY_PRODUCT)
    comment_status = models.CharField(max_length=15, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    approved = ProductCommentManager()

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = _('کامنت محصولات')
        verbose_name_plural = _('کامنت های محصولات')

    def __str__(self):
        return self.title

    def get_suggest_product(self):
        if self.suggest_buy_product == self.I_DONT_SUGGEST:
            return 'no'
        elif self.suggest_buy_product == self.I_SUGGEST:
            return 'yes'
        else:
            return 'no_idea'

    def get_comment_status(self):
        if self.comment_status == ProductComment.COMMENT_STATUS_APPROVED:
            return 'approved'
        elif self.comment_status == ProductComment.COMMENT_STATUS_WAITING:
            return 'waiting'
        else:
            return 'not_approved'


class ProductCommentScore(models.Model):
    SCORE = [
        ('l', _('like')),
        ('dl', _('dislike')),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like')
    comment = models.ForeignKey(ProductComment, on_delete=models.CASCADE, related_name='scores')
    score = models.CharField(max_length=3, choices=SCORE)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment.title} {self.score}'
