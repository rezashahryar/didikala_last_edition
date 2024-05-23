from django.urls import path
from . import views

# create your urls here

app_name = 'comments'

urlpatterns = [
    path('add/comment/post/<slug:slug>/', views.create_comment_view, name='add_comment_post'),
    path('score/<slug:slug>/', views.create_score, name='create_score'),
]