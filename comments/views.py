from django.contrib import messages
from posts.models import Post
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .models import PostComment, PostCommentScore
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
