from django.contrib import admin
from django.urls import path
from  .import views
from .views import  DairyListView


urlpatterns = [
    # path('', views.classdairy, name='classdairy'),
    # path('create-dairy/', views.classDairyCreate.as_view(), name='classdairy-create'),
    path('create-dairy/', views.saveDairy, name='classdairy-create'),
    path('<int:id>/delete-dairy/', views.deleteDairy, name='classdairy-delete'),
    path('<int:id>/update-dairy/', views.updateDairy, name='classdairy-update'),
    path('user/<str:username>', views.DairyListView.as_view(), name='user-view-classdairy'),
]