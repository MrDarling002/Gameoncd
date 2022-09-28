from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nickname", required = True,widget = forms.TextInput(attrs={'class' : 'form-control valid'}))
    password1 = forms.CharField(label="Password", required = True,widget = forms.PasswordInput(attrs={'class' : 'form-control valid'}))
    password2 = forms.CharField(label="Repeat password", required = True,widget = forms.PasswordInput(attrs={'class' : 'form-control valid'}))
    email = forms.EmailField(label="Email", required = True,widget = forms.TextInput(attrs={'class' : 'form-control valid'}))
    first_name = forms.CharField(label="Name", required = True,widget = forms.TextInput(attrs={'class' : 'form-control valid'}))
    last_name = forms.CharField(label="Surname", required = True,widget = forms.TextInput(attrs={'class' : 'form-control valid'}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", 'password2', "username")
        
    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            return user