from django.urls import path
# from .views import BehaviourListView
from  .import views
urlpatterns = [
    path('pending/', views.PendingList.as_view(), name='pending-reqest'),
    path('accepting/', views.AcceptReq.as_view(), name='accepting'),
]