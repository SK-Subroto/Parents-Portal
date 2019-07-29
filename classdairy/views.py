from django.shortcuts import render, get_object_or_404,HttpResponse, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView
# from django.contrib.auth.models import User
from users.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Classdairy
from .utils import Calendar
from django.utils.safestring import mark_safe
from django.forms import ModelForm
import calendar
from datetime import datetime, timedelta, date
from users.models import User
from users.decorators import teacher_required, parent_required


def DairyListView(request):
    queryset = Classdairy.objects.filter(author__id = request.user.id)
    context = {
        'queryset': queryset
    }
    return render(request,'classdairy/classdairy.html', context)

# class DairyListView(ListView):
#     queryset = Classdairy.objects.all()
#     model = Classdairy
#     template_name = 'classdairy/classdairy.html'
#     context_object_name = 'queryset'
#     # paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Classdairy.objects.filter(author=user)



class classDairyCreate(LoginRequiredMixin, CreateView):
    model = Classdairy
    success_url = '/classdairy/dairyTeacher/'
    fields = ['date_post', 'content', 'subject']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# def saveDairy(request):
#     if request.method=='POST':
#         classDairy=Classdairy(author=request.user,date_post=request.POST['date_post'],content=request.POST['content'],subject=request.POST['subject'])
#         classDairy.save()
#         return redirect('/classdairy/user/adity')
#     return HttpResponse("success")


def deleteDairy(request, id):
    dairy = get_object_or_404(Classdairy, pk=id)
    dairy.delete()
    return redirect("/classdairy/dairyTeacher/")

# def updateDairy(request, id):
#     obj = get_object_or_404(Classdairy, pk=id)
#     form = DairyForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         redirect('/classdairy/user/sk')
#     return HttpResponse("success" )

class ClassDairyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Classdairy
    fields = ['date_post','content', 'subject']
    success_url = '/classdairy/dairyTeacher/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

##Parents
class ParentsDairyListView(ListView):
    queryset = Classdairy.objects.all()
    model = Classdairy
    template_name = 'classdairy/classdairyParents.html'
    context_object_name = 'queryset'
    ordering = ['-date_post']
    # paginate_by = 5


#calender
class CalendarView(ListView):
    model = Classdairy
    template_name = 'classdairy/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class CalenderDetailView(DetailView):
    model = Classdairy


class ClassDairyReplyUpdateView(LoginRequiredMixin, UpdateView):
    model = Classdairy
    fields = ['check', 'comment']
    success_url = '/classdairy/classDairyParentView'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False