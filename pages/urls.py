from django.urls import path
from . import views

# create your urls here

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('page-faq/', views.PageFaqView.as_view(), name='page_faq'),
    path('page-faq-question/', views.PageFaqQuestionView.as_view(), name='page_faq_question'),
    path('page-faq-category/', views.PageFaqCategoryView.as_view(), name='page_faq_category'),
    path('page-privacy/', views.PagePrivacyView.as_view(), name='page_privacy'),
]
