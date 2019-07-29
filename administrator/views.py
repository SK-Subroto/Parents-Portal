from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# from django.contrib.auth.models import User
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from parents_portal.roles import Administrator


class PendingList(View, LoginRequiredMixin):
    
    def get(self, request, *args, **kwargs):
        queryset = {'users' : User.objects.filter(is_active=False)}
        return render(request, 'administrator/pendingUser.html', queryset)

class AcceptReq(View, LoginRequiredMixin):
    

    def get(self, request, *args, **kwargs):
         user = User.objects.get(id = 6)
         return assign_role(user, 'administrator')
         