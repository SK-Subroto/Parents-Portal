from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, ListView
# from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from parents_portal.roles import Administrator


class PendingList(View, LoginRequiredMixin):
    
    def get(self, request, *args, **kwargs):
        queryset = {'users' : User.objects.filter(is_active=False)}
        return render(request, 'administrator/pendingUser.html', queryset)

class AcceptReq(View, LoginRequiredMixin):
    # model = User
    # template_name = 'administrator/pendingUser.html'
    
    def get(self, request):
        user = User.objects.get(id = self.request.GET.get('p'))
        user.is_active = True
        user.is_active.save()
        queryset = {'users' : User.objects.filter(is_active=False)}
        return render(request, 'administrator/pendingUser.html', queryset)