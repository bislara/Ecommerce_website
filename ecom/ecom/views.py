from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from ecom.forms import ContactForm,LoginForm,RegisterForm

def home_page(request):
    # return HttpResponse ("HI WORLD !!")
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the Home page",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Hey I am a student"
    return render(request,"home_page.htm",context)



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "title":"HELLO WORLD",
        "content":"Welcome to the about page",
        "form":form
    }
    print("User Logged IN")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request,"auth/login.htm",context)

User = get_user_model()
def registration_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "auth/registration.htm", context)


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