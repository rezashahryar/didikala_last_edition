from django.urls import path
from . import views

# create your urls here

app_name = 'posts'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='post_list'),
]
