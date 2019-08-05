from django.urls import path
# from .views import BehaviourListView
from  .import views
urlpatterns = [
    path('viewbahave/', views.BehaviourListView, name='user-view-behaviour'),
    path('behaviour/new/', views.BehaveCreateView.as_view(), name = 'behavior-create'),
    path('behaviour/<int:pk>/update', views.BehaveUpdateView.as_view(), name = 'behavior-update'),
    path('behaviour/<int:pk>/delete', views.BehaveDeleteView.as_view(), name = 'behavior-delete'),
    path('ranklist/', views.RanklistView, name='behave_rank'),
    path('behaveParentView/', views.ParentsBehaveListView.as_view(), name='parents-view-behaviour'),
    path('<int:pk>/Parents-update-dairy/', views.BehaveReplyUpdateView.as_view(template_name='behaviour/behavior_parent_form.html'), name='parents-behavior-update'),
   ]