from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type =[("1", "Parent"), ("2", "Teacher")]
    choices = forms.ChoiceField(choices=user_type, label="Type")
    is_approve = forms.BooleanField(initial=False, widget = forms.HiddenInput(), required = False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'choices', 'is_approve']