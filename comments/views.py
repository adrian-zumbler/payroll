from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import Comment
from django.core import serializers
import json
class CommentCreateView(View):

    def post(self,request):
        date = request.POST.get('day')
        text = request.POST.get('comment')
        validate = False
        user = User.objects.get(id = request.user.id)

        comment = Comment.objects.create(
            date =  date,
            text = text,
            validate =  validate,
            user = user,
        )
        comment.save()

        return JsonResponse({'success': 'The comment has been sended succesfull'})

class CommentList(View):

    def post(self,request):
        date = request.POST.get('day')
        comment = Comment.objects.filter(date=date)
        data = serializers.serialize('json',comment)

        return HttpResponse(data)

    def get(self,request):
        comment = Comment.objects.all().filter(validate=False)
        data = serializers.serialize('json',comment)

        return HttpResponse(data);





# Create your views here.
