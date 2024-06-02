from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

from posts.models import Post
from products.models import Product

from .models import PostComment, PostCommentScore, GoodPoint, WeakPoint, ProductComment, ProductCommentScore, ProductPoints
from .forms import CommentForm
# Create your views here.


@login_required
@require_GET
def create_score(request, slug):
    type = request.GET.get('type')
    if type == 'l':
        second_type = 'dl'
    elif type == 'dl':
        second_type = 'l'
    comment_id = request.GET.get('comment_id')
    comment = get_object_or_404(PostComment, pk=comment_id)
    try:
        score = PostCommentScore.objects.get(comment_id=comment_id, user_id=request.user.id, score=type)
        score.delete()

        messages.success(request, 'امتیاز شما با موفقیت حذف شد')

    except PostCommentScore.DoesNotExist:
        try:
            tscore = PostCommentScore.objects.get(comment_id=comment_id, user=request.user.id, score=second_type)
            tscore.delete()
        except PostCommentScore.DoesNotExist:
            tscore = None
        PostCommentScore.objects.create(comment=comment, user=request.user, score=type)
        messages.success(request, 'امتیاز شما با موفقیت برای کامنت اعمال شد')

    return redirect('posts:post_detail', slug)


@login_required()
@require_POST
def create_comment_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.user = request.user
            new_form.save()
            return redirect('posts:post_detail', slug)
        

@login_required
@require_GET
def create_score_product_comment(request, slug):
    type = request.GET.get('type')
    if type == 'l':
        second_type = 'dl'
    elif type == 'dl':
        second_type = 'l'
    comment_id = request.GET.get('comment_id')
    comment = get_object_or_404(ProductComment, pk=comment_id)
    try:
        score = ProductCommentScore.objects.get(comment_id=comment_id, user_id=request.user.id, score=type)
        score.delete()

        messages.success(request, 'امتیاز شما با موفقیت حذف شد')

    except ProductCommentScore.DoesNotExist:
        try:
            tscore = ProductCommentScore.objects.get(comment_id=comment_id, user=request.user.id, score=second_type)
            tscore.delete()
        except ProductCommentScore.DoesNotExist:
            tscore = None
        ProductCommentScore.objects.create(comment=comment, user=request.user, score=type)
        messages.success(request, 'امتیاز شما با موفقیت برای کامنت اعمال شد')

    return redirect('products:product_detail', slug)


@login_required
def add_comment_product(request, pk):
    get_product = get_object_or_404(Product.objects.filter(available=True), pk=pk)
    print(request.POST)
    if request.method == 'POST':
        form = ProductComment()
        form.user = request.user
        form.product = get_product
        form.title = request.POST.get('title')
        form.text = request.POST.get('text')
        form.suggest_buy_product = request.POST.get('suggest_buy_product')
        form.save()
        print('=+' * 90)
        print(request.POST)
        queryset = dict(request.POST)
        for i in queryset.get('comment[advantages][]'):
            good_point = GoodPoint()
            good_point.good_point = i
            good_point.save()

        for i in queryset.get('comment[disadvantages][]'):
            weak_point = WeakPoint()
            weak_point.weak_point = i
            weak_point.save()

            product_points = ProductPoints()
            product_points.comment = get_object_or_404(ProductComment.objects.all(), pk=form.pk)
            product_points.save()
            productGoodPoint = get_object_or_404(ProductPoints, pk=product_points.pk)
            productGoodPoint.good_point.add(good_point)
            productGoodPoint.weak_point.add(weak_point)
            productGoodPoint.save()

        return redirect('products:product_detail', get_product.slug)

    context = {
        'product': get_product,
    }
    return render(request, 'comments/add_comment_product.html', context)
