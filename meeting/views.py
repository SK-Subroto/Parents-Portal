from django.shortcuts import render
from .models import Meeting
from student.models import Student
from parents.models import Parents
from users.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class MeetingCreate(LoginRequiredMixin, CreateView):
    model = Meeting
    success_url = '/meeting/meetingTeacher/'
    fields = ['student','date','message']

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

#teacher
def MeetingListView(request):
    queryset = Meeting.objects.filter(teacher__id=request.user.id)
    context = {
        'meetings': queryset
    }
    return render(request, 'meeting/meetingView.html', context)


class MeetingUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Meeting
    success_url = '/meeting/meetingTeacher/'
    fields = ['student', 'date', 'message']

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.teacher:
            return True
        return False

class MeetingDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meeting
    success_url = '/meeting/meetingTeacher/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.teacher:
            return True
        return False


#parents
def MeetingParents(request):
    stuId = Parents.objects.filter(user__id=request.user.id).first()
    queryset = Meeting.objects.filter(student__stu_id = stuId.stu_id.stu_id)
    context = {
        'meetingP': queryset
    }
    return render(request,'meeting/meetingParents.html', context)