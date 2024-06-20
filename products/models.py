from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from random import randint

from tinymce.models import HTMLField
# Create your models here.


class Color(models.Model):
    title = models.CharField(_('عنوان'), max_length=100)
    code_of_color = models.CharField(max_length=100, help_text=_('لطفا کد رنگ را بدون علامت # وارد کنید'), blank=True)

    class Meta:
        verbose_name = _('color')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(_('عنوان'), max_length=100)

    class Meta:
        verbose_name = _('brand')

    def __str__(self):
        return self.title[:15]


class ProductProperties(models.Model):
    title = models.CharField(_('عنوان'), max_length=100)

    class Meta:
        verbose_name = _('property')
        verbose_name_plural = _('properties')

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    properties = models.ManyToManyField(ProductProperties, verbose_name=_('ویژگی ها'))
    title = models.CharField(_('عنوان'), max_length=100)
    slug = models.SlugField(_('مسیر یو ار ال'), unique=True, null=True, blank=True)
    picture = models.ImageField(_('عکس'), upload_to='category_pictures')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def get_absolute_url(self):
        return reverse('products:category_objects_view', args=[self.slug])

    def __str__(self):
        return self.title[:15]


class SubProductCategory(models.Model):
    main_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='children', verbose_name=_('دسته بندی اصلی'))
    title = models.CharField(_('عنوان'), max_length=100)
    slug = models.SlugField(_('مسیر یو ار ال'), unique=True)

    class Meta:
        verbose_name = _('sub_category')
        verbose_name_plural = _('sub_categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:sub_category_objects_view', args=[self.main_category.slug, self.slug])
    

class SubSubProductCategory(models.Model):
    main_sub_category = models.ForeignKey(SubProductCategory, on_delete=models.CASCADE, related_name='sub_children', verbose_name=_('دسته بندی اصلی'))
    title = models.CharField(_('عنوان'), max_length=100)
    slug = models.SlugField(_('مسیر یو ار ال'), unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:sub_sub_category_objects_view', args=[
            self.main_sub_category.main_category.slug,
            self.main_sub_category.slug,
            self.slug,
        ])


def random_number():
    num = int(randint(1000, 100000))
    return str(num)


class ProductImages(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images', null=True)
    image = models.ImageField(upload_to='images-products/', blank=True)


class ProductMovie(models.Model):
    movie = models.FileField(upload_to='product/movies')


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name=_('دسته بندی'))
    sub_category = models.ForeignKey(SubProductCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='products', verbose_name=_('دسته بندی فرعی'))
    sub_sub_category = models.ForeignKey(SubSubProductCategory, on_delete=models.CASCADE, related_name='products', null=True)
    title = models.CharField(_('عنوان'), max_length=100)
    slug = models.SlugField(_('مسیر یو ار ال'), unique=True, null=True)
    product_code = models.CharField(_('کد محصول'), max_length=8, default=random_number)

    inventory = models.IntegerField(default=0)
    available = models.BooleanField(_('موجود'), default=True)

    cover = models.ImageField(_('عکس'), upload_to='products/covers')
    movie = models.ForeignKey(ProductMovie, null=True, blank=True, on_delete=models.CASCADE, related_name='product_movies')

    color = models.ManyToManyField(Color, related_name='colors', verbose_name=_('رنگ'))
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands', verbose_name=_('برند'))

    discount = models.PositiveIntegerField(_('تخفیف'), null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    price = models.IntegerField(_('قیمت'))
    description = HTMLField(verbose_name=_('توضیحات'))
    counted_views = models.IntegerField(_('تعداد بازدید'), default=0)

    sales_number = models.PositiveIntegerField(_('تعداد فروش'), default=0)

    datetime_created = models.DateTimeField(_('created_date'), auto_now_add=True)
    datetime_updated = models.DateTimeField(_('updated_date'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])

    @property
    def get_discount(self):
        if self.discount > 0:
            return True
        return None

    @property
    def best_seller(self):
        if self.sales_number > 1000:
            return True
        else:
            return False
        
    @property
    def get_price(self):
        if self.discount > 0:
            return (self.price - int((self.price * self.discount) / 100))
        else:
            return self.price

    @property
    def get_price_discount_of_product(self):
        return int(self.price * self.discount / 100)

    def get_product_price_after_discount(self):
        price = self.price - int(self.price * self.discount / 100)
        return price


class SetProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties', verbose_name=_('محصول'))
    property = models.ForeignKey(ProductProperties, on_delete=models.CASCADE, verbose_name=_('ویژگی'))
    value = models.CharField(_('مقدار'), max_length=250)

    def __str__(self):
        return f'property {self.property} for {self.product.title} with value {self.value}'


class Question(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='answers', null=True, blank=True, verbose_name=_('parent'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions', verbose_name=_('user'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions', verbose_name=_('product'))
    text = models.TextField(_('text'))

    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ('-datetime_created', )
        verbose_name = _('question')
        verbose_name_plural = _('questions')

    def __str__(self):
        return format_html(
            '<span>{}</span><b> for </b><span>{}</span> product', self.user, self.product
        )
