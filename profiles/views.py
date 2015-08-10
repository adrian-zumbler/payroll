from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import authenticate


class ProfileLoginView(View):

	def get(self,request):
		return render(request,'profiles/login.html')

	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username= username,password = password)
		if user is not None:
			if user.is_active:
				return redirect('/payroll/paid')
		else:
			return redirect('/profile/login')		






