from django.urls import path
#from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.NoticeListView.as_view(), name = 'notice-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('notice/<int:pk>/', views.NoticeDetailView.as_view(), name = 'notice-detail'),
    path('notice/new/',views.NoticeCreateView.as_view(), name = 'notice-create'),
    path('post/<int:pk>/update', views.NoticeUpdateView.as_view(), name = 'notice-update'),
    path('post/<int:pk>/delete', views.NoticeDeleteView.as_view(), name = 'notice-delete'),
    path('parentNotice/', views.NoticeParentListView.as_view(), name = 'notice-parent'),
    path('teacherNotice/', views.NoticeTeacherListView.as_view(), name = 'notice-teacher'),

]