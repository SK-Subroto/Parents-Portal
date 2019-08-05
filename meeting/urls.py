from django.urls import path
from . import views


urlpatterns = [
    path('meetingTeacher/', views.MeetingListView, name = 'meeting_teacher'),
    path('meetingUpdate/<int:pk>/', views.MeetingUpdate.as_view(), name = 'meeting_update'),
    #path('notice/new/',Meeting.as_view(), name = 'meeting-create'),
    path('meetingCreate/', views.MeetingCreate.as_view(), name='create_meeting'),
    path('meetingParents/', views.MeetingParents, name='parents_meeting'),
    path('meetingDelete/<int:pk>/', views.MeetingDelete.as_view(), name='delete_meeting'),


]