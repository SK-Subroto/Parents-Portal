"""parents_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from users import views as user_views
from django.conf.urls.static import static

urlpatterns = [
    path('',include('landing.urls')),
    path('admin/', admin.site.urls),
    path('parents/', include('parents.urls')),
    path('teacher/', include('teacher.urls')),
    path('administrator/', include('administrator.urls')),
    path('student/', include('student.urls')),
    path('classdairy/', include('classdairy.urls')),
    path('progress_report/', include('progress_report.urls')),
    path('behaviour/', include('behaviour.urls')),
    path('notice/',include('notice.urls')),
    path('result/',include('result.urls')),
    path('chat/',include('chat.urls')),
    # path('register/', user_views.register, name='register'),
    path('', user_views.home, name='home'),
    path('accounts/signup/', user_views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/parent/', user_views.ParentSignUpView.as_view(), name='parent_signup'),
    path('accounts/signup/teacher/', user_views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.home, name='profile'),
]

