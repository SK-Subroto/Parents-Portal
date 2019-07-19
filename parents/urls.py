from django.contrib import admin
from django.urls import path, include
from  .import views
# from .views import parentsProfileDetailView


urlpatterns = [
    path('', views.home, name='parents-home'),
    path('profile/', views.profile, name='parents-profile'),
    path('meeting/', views.meeting, name='parents-meeting'),
    # path('dairy/', views.dairy, name='parents-dairy'),
    path('dairy/', views.Dairy.as_view(), name='parents-dairy'),
    path('notice/', views.notice, name='parents-notice'),
    path('result/', views.result, name='parents-result'),
    # path('progressreport/', views.progressreport, name='parents-progressreport'),
]