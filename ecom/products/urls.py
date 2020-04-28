
from django.urls import path

# include all the classes at a time using the ()
from .views import (
                    ProductListView,
                    product_list_view,
                    ProductDetailView,
                    product_detail_view,
                    ProductDetailSlugView,
                    ProductFeaturedView,
                    ProductFeaturedDetailView
                    )

urlpatterns = [
    path('featured/', ProductFeaturedView.as_view(),name='index'),
    path('featured/<int:pk>', ProductFeaturedDetailView.as_view(),name='index'),
    path('', ProductListView.as_view(),name='index'),
    path('products_func/', product_list_view,name='index'),
    path('<int:pk>', ProductDetailView.as_view(),name='index'),
    path('<slug:slug_field>', ProductDetailSlugView.as_view(),name='index'),
    path('products_func/<int:pk>', product_detail_view,name='index'),
]
