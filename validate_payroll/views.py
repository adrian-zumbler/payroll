from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from .models import ValidatePayroll
from django.http import HttpResponse
from django.http import JsonResponse

class ValidatePayrollView(View):

    def post(self,request):
        date = request.POST.get('day')
        user = User.objects.get(id = request.user.id)
        try:
            validate = ValidatePayroll.objects.get(date=date,user__id = user.id)
            return JsonResponse({'exist': True })
        except Exception :
            return JsonResponse({'exist': False })


    def get(self,request):

        return JsonResponse({'validate': True})
