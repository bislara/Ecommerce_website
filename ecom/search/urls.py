
from django.urls import path

# include all the classes at a time using the ()
from search.views import (
                    ProductSearchView,
                    )

urlpatterns = [
    path('', ProductSearchView.as_view(),name='query'),
]
