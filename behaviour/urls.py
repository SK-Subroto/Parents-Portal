from django.urls import path
# from .views import BehaviourListView
from  .import views
urlpatterns = [
    path('viewbahave/', views.BehaviourListView.as_view(), name='user-view-behaviour'),
    path('behaviour/new/', views.BehaveCreateView.as_view(), name = 'behavior-create'),
    path('behaviour/<int:pk>/update', views.BehaveUpdateView.as_view(), name = 'behavior-update'),
    path('behaviour/<int:pk>/delete', views.BehaveDeleteView.as_view(), name = 'behavior-delete'),
    path('ranklist/', views.RanklistView, name='behave_rank'),
    path('behaveParentView/', views.ParentsBehaveListView.as_view(), name='parents-view-behaviour'),
    path('<int:pk>/Parents-update-dairy/', views.BehaveReplyUpdateView.as_view(template_name='behaviour/behavior_parent_form.html'), name='parents-behavior-update'),
    path('search/',views.SearchPageView.as_view(), name='student_search'),
    path('searchResult/', views.SearchResultsView.as_view(), name='search_results'),
    path('behaveAssess/', views.BehaveAssessCreateView.as_view(), name='behave_assess'),
    path('behaveAssessViewTeach/', views.BehaviourAssesTeachListView.as_view(), name='behave_assess_view'),
    path('behaveAssessViewParent/', views.BehaviourAssesParentListView.as_view(), name='behave_assess_parent_view'),
    path('SelectMothYear/',views.SelectMothYear.as_view(), name='select_month'),
   ]