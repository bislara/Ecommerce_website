
from django.urls import path

# include all the classes at a time using the ()
from .views import (
                    cart_home,
                    cart_update
                )

urlpatterns = [
    path('', cart_home,name='home'),
    path('update/', cart_update,name='update'),
]
