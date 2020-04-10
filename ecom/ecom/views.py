from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

def home_page(request):
    # return HttpResponse ("HI WORLD !!")
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the Home page"
    }
    return render(request,"home_page.htm",context)


def about_page(request):
    # return HttpResponse ("HI WORLD !!")
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the about page"
    }
    return render(request,"home_page.htm",context)

def contact_page(request):
    # return HttpResponse ("HI WORLD !!")
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the contact page"
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("fullname"))
        print(request.POST.get("email"))
        print(request.POST.get("content"))
    return render(request,"contact/view.htm",context)