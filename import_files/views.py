from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings

class ImportView(View):

    def get(self,request):
        if request.user.is_authenticated():
<<<<<<< HEAD
			return render(request, 'importFiles/import.html')
=======
            if request.user.is_staff:
                return render(request, 'importFiles/import.html')
            else:
                return redirect(settings.LOGIN_URL)
>>>>>>> 961c02ecd8d922af191c2f3074c25ff5c0219d89
        else:
			return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
