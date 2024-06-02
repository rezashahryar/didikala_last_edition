from django import forms
from .models import PostComment, ProductComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['title', 'text']


class CommentProductForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['title', 'text']
