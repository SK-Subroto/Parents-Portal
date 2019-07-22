from django.urls import path
# from .views import BehaviourListView
from  .import views
urlpatterns = [
    path('', views.Landing, name='landng'),
       ]