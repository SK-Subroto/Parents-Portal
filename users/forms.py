from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
# from .models import Profile


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     user_type =[("1", "Parent"), ("2", "Teacher")]
#     choices = forms.ChoiceField(choices=user_type, label="Type")
#     is_active = forms.BooleanField(initial=False, widget = forms.HiddenInput(), required = False)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'choices', 'is_active']


from .models import User


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class ParentSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     # queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.is_active = False
        user.save()
        # student = Student.objects.create(user=user)
        # student.interests.add(*self.cleaned_data.get('interests'))
        return user