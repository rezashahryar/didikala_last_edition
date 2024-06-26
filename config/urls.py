"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('core.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('comments/', include('comments.urls')),
    path('post/', include('posts.urls')),
    path('product/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('profile/', include('profiles.urls')),
    path('order/', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),

    # django summer note pack
    path('summernote/', include('django_summernote.urls')),
    # django debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
    # tiny-mce text editor pack
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
