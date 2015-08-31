from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout


class ProfileLoginView(View):

	def get(self,request):

		if request.GET.get('next',False):
			return render(request,'profiles/login.html',{'next' : request.GET['next']})
		else:
			return render(request,'profiles/login.html')



	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username= username,password = password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('/payroll/day/')
		else:
			return redirect('/profile/login')

class ProfileLogoutView(View):

	def get(self, request):
		logout(request)
		return redirect('/profile/login')
