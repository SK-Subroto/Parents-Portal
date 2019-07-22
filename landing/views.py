from django.shortcuts import render

def Landing(request):
    return render (request,'landing/index.html')
