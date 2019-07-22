from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from result.models import Result
from student.models import Student
from admission.models import Admission
from django.contrib.auth.models import User

# def progressReport(request):
#     return render(request, 'progress_report/progressreport.html')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'progress_report/charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    
    # stu = Student.objects.get(user = request.user)
    # adm = Admission.objects.filter(student = stu).first()
    # res = Result.objects.get(admission_id = adm.id)
    res=Result.objects.filter(admission_id__student__user__id = request.user.id)
    
    data = {
        "sales": 12,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    
    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        # q = Result.objects.get(id=2)
        total_result = []
        res=Result.objects.filter(admission_id__student__user__id = 1)
        for cnt in range(res.count()):
            total_result.append(res[cnt].first_mark + res[cnt].second_mark + res[cnt].third_mark)
        labels = ["1st Term", "2nd Term", "3rd Term"]
        # default_items = [200,300,275]
        
        default_items = [total_result[0], total_result[1], total_result[2]]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


class BarData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        res=Result.objects.filter(admission_id__student__user__id = 1)
        labels = ["Bangla", "English", "Math"]
        default_items = [[92,90,95], [res[0].first_mark, res[1].first_mark, res[2].first_mark]]
        data = {
                "labelsBar": labels,
                "defaultBar": default_items,
        }
        return Response(data)