from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your full name"
                    }
                    )
            )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Your email"
                    }
                    )
            )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message" 
                    }
                )
            )

# Always return a value to use as the new cleaned data, even if
# this method didn't change it.
    def clean_fullname(self):
        name = self.cleaned_data.get("fullname")
        if name == "" or len(name)<=1:
            raise forms.ValidationError("Enter a valid name")
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "@" or not ".com" in email:
            raise forms.ValidationError("Email must have @ and .com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)    
    password = forms.CharField(widget=forms.PasswordInput)    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)    
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data