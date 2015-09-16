from django.shortcuts import render
from django.views.generic import View
from .models import Period
from django.core import serializers
from django.http import HttpResponse


class PeriodListView(View):

    def get(self,request):
        periods = Period.objects.all().order_by('-start_date')
        data = serializers.serialize('json',periods)
        return HttpResponse(data)
