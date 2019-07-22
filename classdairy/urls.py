from django.contrib import admin
from django.urls import path
from  .import views
from .views import  DairyListView, ClassDairyUpdateView,ParentsDairyListView, ClassDairyReplyUpdateView


urlpatterns = [
    # path('', views.classdairy, name='classdairy'),
    # path('create-dairy/', views.classDairyCreate.as_view(), name='classdairy-create'),
    path('create-dairy/', views.saveDairy, name='classdairy-create'),
    path('<int:id>/delete-dairy/', views.deleteDairy, name='classdairy-delete'),
    path('<int:pk>/update-dairy/', views.ClassDairyUpdateView.as_view(), name='classdairy-update'),
    path('user/<str:username>', views.DairyListView.as_view(), name='user-view-classdairy'),
    path('classDairyParentView/', views.ParentsDairyListView.as_view(), name='parents-view-classdairy'),
    path('<int:pk>/Parents-update-dairy/', views.ClassDairyReplyUpdateView.as_view(template_name='classdairy/parents_classdairy_form.html'), name='parents-classdairy-update'),
]