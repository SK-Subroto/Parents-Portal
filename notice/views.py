from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
# from django.contrib.auth.models import User
from users.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Notice
#decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.decorators import teacher_required, parent_required


def noticeHome(request):
    context = {'notices': Notice.objects.all()}
    return render (request,'notice/noticehome.html',context)


class NoticeListView(ListView):
    allowed_roles = 'administrator'
    model = Notice
    template_name='notice/noticehome.html'
    context_object_name = 'notices'
    ordering = ['-date_posted']

class NoticeDetailView(DetailView):
    model= Notice

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    success_url='/notice/'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    success_url='/notice/'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    success_url = '/notice/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#parents notice
@method_decorator([login_required, parent_required], name='dispatch')
class NoticeParentListView(ListView):
    model = Notice
    template_name='notice/noticeParent.html'
    context_object_name = 'notices'
    ordering = ['-date_posted']

#teacher notice
class NoticeTeacherListView(ListView):
    model = Notice
    template_name='notice/noticeTeacher.html'
    context_object_name = 'notices'
    ordering = ['-date_posted']
