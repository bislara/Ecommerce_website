from django.shortcuts import render, redirect

from .models import Cart
from products.models import Product


# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print('New Cart created')
#     return cart_obj

def cart_home(request):
    if request.user.is_authenticated:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        request.session['cart_items'] = cart_obj.products.count()
        return render(request,"carts/view.htm",{"cart": cart_obj})
    else:
        return render(request,"carts/view.htm",{"cart": None})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request)
            if product_obj in cart_obj.products.all():
                cart_obj.products.remove(product_obj)
            else:
                cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
            request.session['cart_items'] = cart_obj.products.count()
        else:
            return redirect("cart:home")
    # return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")