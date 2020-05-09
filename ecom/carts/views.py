from django.shortcuts import render, redirect

from addresses.forms import AddressForm
from billing.models import BillingProfile
from .models import Cart
from products.models import Product
from orders.models import Order

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

def checkout_home(request):
    if request.user.is_authenticated:
        cart_obj, cart_created = Cart.objects.new_or_get(request)
        order_obj = None
        if cart_created or cart_obj.products.count() == 0:
            return redirect("cart:home")
        # else:
        #     order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
        user = request.user
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
                                                            user=user, email=user.email)
        address_form = AddressForm()

        if billing_profile is not None:
            order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
            
    else:
        return redirect("cart:home")
    
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "address_form": address_form,
    }

    return render(request, "carts/checkout.htm", context)