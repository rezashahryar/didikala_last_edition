from django.urls import path
from . import views

# create your urls here

app_name = 'comments'

urlpatterns = [
    path('add/comment/post/<slug:slug>/', views.create_comment_view, name='add_comment_post'),
    path('score/post/<slug:slug>/', views.create_score, name='create_score'),
    path('add/comment/product/<int:pk>/', views.add_comment_product, name='add_comment_product'),
    path('score/product/<slug:slug>/', views.create_score_product_comment, name='create_score_product'),
]