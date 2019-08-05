from django.urls import path
#from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.resultSearch, name = 'result_search'),
    path('viewResult/', views.viewResult, name = 'view_result'),

]