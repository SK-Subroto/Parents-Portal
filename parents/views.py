from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Parents


obj = Parents.objects.get(id = 1)

def home(request):
   
    return render(request, 'parents/dashboard.html' )

@login_required
def profile(request):
    return render(request, 'parents/profile.html' )


def meeting(request):
    return render(request, 'parents/meeting.html', {'title':'meeting'} )

# def dairy(request):
#     return render(request, 'parents/classDairy.html', {'title':'dairy'} )
class Dairy(generic.TemplateView):
    template_name = 'parents/classDairy.html'
    

    def get(self, request):
        context={
        'name' : obj.name
    }
        return render(request, self.template_name, context)


def notice(request):
    return render(request, 'parents/notice.html', {'title':'notice'} )

def result(request):
    return render(request, 'parents/result.html', {'title':'result'} )

def progressreport(request):
    return render(request, 'parents/progressreport.html', {'title':'progressreport'} )