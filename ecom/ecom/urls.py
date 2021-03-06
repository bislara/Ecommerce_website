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
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from accounts.views import login_page,registration_page
from addresses.views import checkout_address_create_view,checkout_address_reuse_view
from .views import home_page,about_page,contact_page
from carts.views import cart_detail_api_view
# or from ecom.views import home_page
from django.views.generic import TemplateView
# from carts.views import cart_home

urlpatterns = [
    path('', home_page,name='home'),
    path('about/', about_page,name='about'),
    path('login/', login_page,name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('example/', TemplateView.as_view(template_name='bootstrap/example.htm')),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),

    # namespace is added so that if any other app is having same url it can work in direct way.
    # include is having a tuple now as we are using namespace now. 2nd argument is the app name to be used
    path('carts/', include(("carts.urls","carts"), namespace = "cart")),
    path('api/cart/', cart_detail_api_view, name = "api-cart"),
    path('products/', include(("products.urls","products"), namespace = "products")),
    path('search/', include(("search.urls","search"), namespace = "search")),
    path('register/', registration_page,name='register'),
    path('contact/', contact_page,name='contact'),
    path('admin/', admin.site.urls),
]

# include the static and media contents in the url
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)