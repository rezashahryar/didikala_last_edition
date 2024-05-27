from django.urls import path
from . import views

# create your urls here

app_name = 'posts'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.CategoryObjectView.as_view(), name='category_objects'),
    path('tag/<slug:slug>/', views.TagObjectView.as_view(), name='tag_objects'),
]
