from django.contrib import admin
from .models import PostComment, ProductCommentScore, WeakPoint, GoodPoint, ProductPoints, ProductComment
# Register your models here.


admin.site.register(PostComment)



@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'product', 'comment_status', 'suggest_buy_product')
    list_editable = ('comment_status', 'suggest_buy_product')

admin.site.register(ProductPoints)
admin.site.register(GoodPoint)
admin.site.register(WeakPoint)
admin.site.register(ProductCommentScore)