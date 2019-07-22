from django.shortcuts import render, get_object_or_404,HttpResponse, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Behavior
from django.forms import ModelForm


class BehaviourListView(ListView):
    queryset = Behavior.objects.all()
    model = Behavior
    template_name = 'behaviour/behaviourTeacher.html'
    context_object_name = 'queryset'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Behavior.objects.filter(author=user)


class BehaveCreateView(LoginRequiredMixin, CreateView):
    model = Behavior
    success_url = "/behaviour/user/sk"
    fields = ['student','date_post','catagory', 'scale', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BehaveUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Behavior
    success_url = "/behaviour/user/sk"
    fields = ['catagory', 'scale', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class BehaveDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Behavior
    success_url = "/behaviour/user/sk"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


##Parents
class ParentsBehaveListView(ListView):
    queryset = Behavior.objects.all()
    model = Behavior
    template_name = 'behaviour/behaviourParents.html'
    context_object_name = 'queryset'
    ordering = ['-date_post']
    # paginate_by = 5


class BehaveReplyUpdateView(LoginRequiredMixin, UpdateView):
    model = Behavior
    fields = ['check']
    success_url = '/behaviour/behaveParentView/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False