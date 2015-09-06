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
        comments = []
        date = reques.POST.get('day')
        for comment in Comments.objects.filter(validate=False).filter(date=date):
            data = {}
            data['text'] = comment.text
            data['date'] = comment.date
            data['user'] =  comment.user.username
            data['validate'] = comment.validate
            comments.append(data)

        return HttpResponse(json.dumps(comments))

    def get(self,request):
        comments = []
        for comment in Comment.objects.filter(validate=False):
            data = {}
            data['id'] = comment.id
            data['text'] = comment.text
            data['date'] = str(comment.date)
            data['user'] =  comment.user.username
            data['validate'] = comment.validate
            comments.append(data)

        return HttpResponse(json.dumps(comments))

class CommentView(View):

    def get(self,request):
        return render(request,'comments/commentsList.html')







# Create your views here.
