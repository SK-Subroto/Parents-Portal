from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import teacher_required, parent_required
# from .forms import UserRegisterForm
from django.views.generic import CreateView, TemplateView
from .forms import TeacherSignUpForm, ParentSignUpForm
from .models import User


class SignUpView(TemplateView):
    template_name = 'landing/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_parent:
            return redirect('parents-home')
        elif request.user.is_teacher:
            return redirect('teacher-home')
        else:
            return redirect('pending-reqest')
    # return render(request, 'user/login.html')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        return redirect('login')


class ParentSignUpView(CreateView):
    model = User
    form_class = ParentSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        return redirect('login')


