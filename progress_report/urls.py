from django.contrib import admin
from django.urls import path
from .views import HomeView, get_data, ChartData, BarData

urlpatterns = [
    # path('', views.progressReport, name='progress-report'),
    path('', HomeView.as_view(), name='home'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data/', ChartData.as_view()),
    path('api/bar/data/', BarData.as_view()),
   
]