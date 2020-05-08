from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from ecom.forms import ContactForm

def home_page(request):
    # return HttpResponse ("HI WORLD !!")
    context = {
        "title":"This website has a collection of lots of garments",
        "content":"Go to the products page to know more",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Hey I am a student"
    return render(request,"home_page.htm",context)

def about_page(request):
    # return HttpResponse ("HI WORLD !!")
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the about page"
    }
    return render(request,"home_page.htm",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the contact page",
        "form": contact_form
    }

    # Django creates an attribute called cleaned_data , a dictionary which contains cleaned data only from the fields which have passed the validation tests. Note that cleaned_data attribute will only be available to you after you have invoked the is_valid() method.
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request,"contact/view.htm",context)