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
    return render(request,"home_page.htm",context)