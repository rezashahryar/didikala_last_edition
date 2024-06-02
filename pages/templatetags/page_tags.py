from django import template
from products.models import ProductCategory
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('includes/count_product_category.html')
def count_product_for_each_category():
    categories = ProductCategory.objects.prefetch_related('products').annotate(products_count=Count('products'))
    return {'categories_navbar': categories}
