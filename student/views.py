from django.shortcuts import render

def home(request):
    return render(request, 'student/home.html', {'title':'home'} )
