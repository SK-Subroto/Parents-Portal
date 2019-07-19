from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from result.models import Result


# def progressReport(request):
#     return render(request, 'progress_report/progressreport.html')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'progress_report/charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    q = Result.objects.get(id=1)
    data = {
        "sales": q.first_mark,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        q = Result.objects.get(id=2)
        labels = ["1st Term", "2nd Term", "3rd Term"]
        # default_items = [200,300,275]
        default_items = [q.first_mark, q.second_mark, q.third_mark]
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
        labels = ["Bangla", "English", "Math"]
        default_items = [[70,90,50], [50,60,40]]
        data = {
                "labelsBar": labels,
                "defaultBar": default_items,
        }
        return Response(data)