from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings

class ImportView(View):

    def get(self,request):
        if request.user.is_authenticated():
			return render(request, 'importFiles/import.html')
        else:
			return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
