from django.shortcuts import render, get_object_or_404,HttpResponse, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Classdairy
from django.forms import ModelForm




#tempClass
class DairyForm(ModelForm):
    class Meta:
        model = Classdairy
        fields = ['date_post', 'content', 'subject']


# def classdairy(request):
#     queryset = Classdairy.objects.all()
#     context = {
#         'queryset': queryset
#     }
#     return render(request,'classdairy/classdairy.html', context)

class DairyListView(ListView):
    queryset = Classdairy.objects.all()
    model = Classdairy
    template_name = 'classdairy/classdairy.html'
    context_object_name = 'queryset'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Classdairy.objects.filter(author=user)



# class classDairyCreate(LoginRequiredMixin, CreateView):
#     model = Classdairy
#     # success_url = '/classdairy/user/sk'
#     fields = ['date_post', 'content', 'subject']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

def saveDairy(request):
    if request.method=='POST':
        classDairy=Classdairy(author=request.user,date_post=request.POST['date_post'],content=request.POST['content'],subject=request.POST['subject'])
        classDairy.save()
        return redirect('/classdairy/user/sk')
    return HttpResponse("success")


def deleteDairy(request, id):
    dairy = get_object_or_404(Classdairy, pk=id)
    dairy.delete()
    return redirect("/classdairy/user/sk")

def updateDairy(request, id):
    obj = get_object_or_404(Classdairy, pk=id)
    form = DairyForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        redirect('/classdairy/user/sk')
    return HttpResponse("success" )

