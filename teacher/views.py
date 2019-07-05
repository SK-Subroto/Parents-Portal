from django.shortcuts import render

def home(request):
    return render(request, 'teacher/dashboard2.html', {'title':'home'} )