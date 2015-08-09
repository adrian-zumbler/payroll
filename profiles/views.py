from django.shortcuts import render
from django.views.generic import View

class ProfileLoginView(View):

	def get(self,request):
		return render(request,'profiles/login.html')
