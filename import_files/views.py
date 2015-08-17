from django.shortcuts import render
from django.views.generic import View

class ImportView(View):

    def get(self,request):
        return render(request, 'importFiles/import.html')
