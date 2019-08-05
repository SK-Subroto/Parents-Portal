from django.shortcuts import render, get_object_or_404,HttpResponse, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
# from django.contrib.auth.models import User
from users.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Behavior
from student.models import Student
from users.models import User
from django.forms import ModelForm
from users.decorators import teacher_required, parent_required

# class BehaviourListView(ListView):
#     queryset = Behavior.objects.all()
#     model = Behavio
#     template_name = 'behaviour/behaviourTeacher.html'
#     context_object_name = 'queryset'

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Behavior.objects.filter(author=user)

def BehaviourListView(requst):
    queryset = Behavior.objects.filter(author__id = requst.user.id)

    context = {
        'queryset': queryset
    }
    return render(requst, 'behaviour/behaviourTeacher.html', context)



class BehaveCreateView(LoginRequiredMixin, CreateView):
    model = Behavior
    success_url = "/behaviour/viewbahave"
    fields = ['student','date_post','catagory', 'scale', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BehaveUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Behavior
    success_url = "/behaviour/viewbahave"
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
    success_url = "/behaviour/viewbahave"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def RanklistView(request):
    stu = Student.objects.all()
    student_id = []
    behave_point = []
    for cnt in range(stu.count()):
        point = Behavior.objects.filter(student__stu_id = stu[cnt].stu_id)
        total_point = 0
        for cnt1 in range(point.count()):
            total_point = total_point + point[cnt1].scale
    
        student_id.append(stu[cnt].stu_id)
        behave_point.append(total_point)
        # behave_point.sort()
    behave_point = zip(stu, behave_point)
    data = {
        # 'students': stu,
        'behave_point': behave_point

    }

    return render(request, 'behaviour/ranklist.html', data)



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