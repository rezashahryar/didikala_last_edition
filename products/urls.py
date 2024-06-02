from django.urls import path
from . import views

# create your urls here

app_name = "products"

urlpatterns = [
    path(
        "detail/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"
    ),
    path(
        "list/category/<slug:cat_slug>",
        views.ProductsOfCategoryListView.as_view(),
        name="category_objects_view",
    ),
    path(
        "list/<slug:category>/<slug:sub_category>/",
        views.ProductOfSubCategoryListView.as_view(),
        name="sub_category_objects_view",
    ),
    path(
        "list/<slug:category>/<slug:sub_category>/<slug:sub_sub_category>/",
        views.ProductOfSubSubCategoryListView.as_view(),
        name="sub_sub_category_objects_view",
    ),
    path("question/<int:pk>/", views.question, name="question"),
    path("answer/<int:pk>/<int:qpk>", views.answer, name="answer"),
]
