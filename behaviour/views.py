from django.shortcuts import render, get_object_or_404,HttpResponse, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
# from django.contrib.auth.models import User
from users.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Behavior
from .models import Behaviour_assess
from student.models import Student
from parents.models import Parents
from users.models import User
from django.forms import ModelForm
from users.decorators import teacher_required, parent_required
# from django.template.loader import render_to_string
# from django.http import JsonResponse
from django.db.models import Q
from .forms import RawBehaveAssessForm

# class BehaviourListView(ListView):
#     queryset = Behavior.objects.all()
#     model = Behavio
#     template_name = 'behaviour/behaviourTeacher.html'
#     context_object_name = 'queryset'

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Behavior.objects.filter(author=user)

# def BehaviourListView(requst):
#     queryset = Behavior.objects.filter(author__id = requst.user.id)

#     context = {
#         'queryset': queryset
#     }
#     return render(requst, 'behaviour/behaviourTeacher.html', context)
class BehaviourListView(ListView):
    model = Behavior
    template_name = 'behaviour/behaviourTeacher.html'
    ordering = ['-date_post']
    
    def get_queryset(self): 
        # stu = Student.objects.filter(stu_id = self.request.GET.get('q')).first()
        # query = self.request.GET.get('q')
        object_list = Behavior.objects.filter( Q(student__stu_id = self.request.GET.get('p')) & Q(author__id = self.request.user.id))
        return object_list


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
        behave_point.sort()
    behave_point = zip(stu, behave_point)
    data = {
        # 'students': stu,
        'behave_point': behave_point

    }

    return render(request, 'behaviour/ranklist.html', data)

# behavior assess
class BehaveAssessCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'behaviour/behavior_assess_form.html'
    
    # success_url = "/behaviour/viewbahave"
    def get(self, request):
        form = RawBehaveAssessForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = RawBehaveAssessForm(request.POST)
        stu = Student.objects.filter(stu_id = self.request.GET.get('q')).first()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.student = stu
            post.save()
            text = form.cleaned_data
            form = RawBehaveAssessForm()
            # return redirect('#')
        context = {'form': form, 'text': text }
        return render(request, self.template_name, context)

class BehaviourAssesTeachListView(ListView):
    model = Behaviour_assess
    template_name = 'behaviour/behavior_assess_teach.html'
    ordering = ['-date_post']
    
    def get_queryset(self): 
        # stu = Student.objects.filter(stu_id = self.request.GET.get('q')).first()
        # query = self.request.GET.get('q')
        object_list = Behaviour_assess.objects.filter(student__stu_id = self.request.GET.get('q'))
        return object_list

        

# def BehaveAssessCreateView(request):
#     form = RawBehaveAssessForm(request.POST or None)
#     student = Student.objects.filter(stu_id = request.GET.get('q'))
#     if form.is_valid():
#         print(form.cleaned_data)
#         form.instance.author = request.user
#         form.instance.student = student
#         Behaviour_assess.objects.create(**form.cleaned_data)
#         # return redirect("report_home")
#     else:
#         print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, "behaviour/behavior_assess_form.html", context)



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

class SelectMothYear(TemplateView):
    template_name = 'behaviour/behaveParentMonth.html'

class BehaviourAssesParentListView(LoginRequiredMixin, ListView):
    model = Behaviour_assess
    template_name = 'behaviour/behavior_assess_parent.html'
    ordering = ['-date_post']
    
    def get_queryset(self):
        month = self.request.GET.get('month')
        # stu = Student.objects.filter(stu_id = self.request.GET.get('q')).first()
        # query = self.request.GET.get('q')
        parent = Parents.objects.filter(user_id = self.request.user.id).first()

        object_list = Behaviour_assess.objects.filter( Q(student__stu_id = parent.stu_id.stu_id) & Q(date_post__month = month))
        return object_list




#behavoir search teacher
class SearchPageView(TemplateView):
    template_name = 'behaviour/behavior_searchbox.html'

class SearchResultsView(ListView):
    model = Behavior
    template_name = 'behaviour/student_list.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Student.objects.filter( Q(name__icontains=query) | Q(stu_id__icontains=query))
        return object_list
    