from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Comment

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

class CommentList(ListView):
    model = Comment
    context_object_name = 'comments_list'
    queryset = Comment.objects.order_by('date')
    template_name = 'comments/commentsList.html'

    



# Create your views here.
