"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import home_page,about_page,contact_page,login_page,registration_page
# or from ecom.views import home_page

# include all the classes at a time using the ()
from products.views import (
                    ProductListView,
                    product_list_view,
                    ProductDetailView,
                    product_detail_view,
                    ProductFeaturedView,
                    ProductFeaturedDetailView
                    )

urlpatterns = [
    path('', home_page,name='index'),
    path('about/', about_page,name='index'),
    path('login/', login_page,name='index'),
    path('featured/', ProductFeaturedView.as_view(),name='index'),
    path('featured/<int:pk>', ProductFeaturedDetailView.as_view(),name='index'),
    path('products/', ProductListView.as_view(),name='index'),
    path('products_func/', product_list_view,name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(),name='index'),
    path('products_func/<int:pk>', product_detail_view,name='index'),
    path('register/', registration_page,name='index'),
    path('contact/', contact_page,name='index'),
    path('admin/', admin.site.urls),
]

# include the static and media contents in the url
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)