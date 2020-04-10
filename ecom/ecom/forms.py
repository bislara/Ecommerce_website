from django import forms

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
