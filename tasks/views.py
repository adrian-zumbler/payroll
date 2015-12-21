from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from django.contrib.auth.models import User
# my models
from agents.models import Agent
from activities.models import Activity
from .models import Task
from django.core.mail import send_mail

#utilities
from datetime import date

class TemplateView(View):

    def get(self,request):
        if request.user.is_staff:
            tasks = Task.objects.filter(status='pendiente')
            activities = Activity.objects.all()
            users = User.objects.all()
            dic = {
                'tasks':tasks,
                'activities':activities,
                'users': users,
            }
            return render(request,'tasks/index.html',dic)
        else:
            return redirect('/profile/login/')

    def post(self,request):
        status = request.POST.get('status')

        print status
        if status == '0':
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(status=status)
        activities = Activity.objects.all()
        users = User.objects.all()
        dic = {
            'tasks':tasks,
            'activities':activities,
            'users': users,
        }
        return render(request,'tasks/index.html',dic)


class CreateTaskView(View):

    def get(self,request):
        user = User.objects.get(id=request.user.id)
        agents = Agent.objects.filter(user__id = user.id)
        activities = Activity.objects.all()
        dic = {
            'agents':agents,
            'activities': activities
        }
        return render(request,'tasks/create-task.html',dic)

    def post(self,request):
        agent = get_object_or_404(Agent,pk=request.POST['agent'])
        activity = get_object_or_404(Activity,pk=request.POST['activity'])
        toDo = request.POST['toDo']
        startTime = request.POST['startTime']
        endTime = request.POST['endTime']
        comment = request.POST['comment']
        user = get_object_or_404(User,pk=request.user.id)

        task = Task.objects.create(
            date_to_do = toDo,
            start_time = startTime,
            end_time = endTime,
            comment = comment,
            agent = agent,
            activity = activity,
            user = user,
            created = date.today().isoformat()

        )
        task.save()

        return redirect('/tasks/list/')

class TaskDetailView(View):

    def get(self,request,id):
        task = get_object_or_404(Task,pk=id)
        dic = {
            'task':task
        }
        return render(request,'tasks/detail-task.html',dic)
class AproveView(View):

    def get(self,reques,id):
        task = get_object_or_404(Task,pk=id)
        task.status = 'aprobado'
        #task.save()
        send_mail('Tarea de %s' %(task.agent.first_name), "<h1>Solicitud fue aprobada</h1>", "wfm@idealccs.com", ["adrian.meza@idealccs.com"], fail_silently=True)
        return redirect('/tasks/')

class DeclineView(View):

    def get(self,reques,id):
        task = get_object_or_404(Task,pk=id)
        task.status = 'rechazada'
        task.save()
        return redirect('/tasks/')

class TaskListView(View):

    def get(self,request):
        user = get_object_or_404(User,pk=request.user.id)
        tasks = Task.objects.filter(status='pendiente').filter(user__id = user.id)
        activities = Activity.objects.all()
        users = User.objects.all()
        dic = {
            'tasks':tasks,
            'activities':activities,
            'users': users,
        }
        return render(request,'tasks/list-task.html',dic)

    def post(self,request):
        user = get_object_or_404(User,pk=request.user.id)
        tasks = Task.objects.filter(status='pendiente').filter(user__id = user.id)
        status = request.POST.get('status')
        if status == '0':
            tasks = Task.objects.all().filter(user__id = user.id)
        else:
            tasks = Task.objects.filter(status=status).filter(user__id = user.id)
        activities = Activity.objects.all()
        users = User.objects.all()
        dic = {
            'tasks':tasks,
            'activities':activities,
            'users': users,
        }
        return render(request,'tasks/list-task.html',dic)

class TaskEditView(View):

    def get(self,request,id):
        task = get_object_or_404(Task,pk=id)
        user = User.objects.get(id=request.user.id)
        agents = Agent.objects.filter(user__id = user.id)
        activities = Activity.objects.all()
        dic = {
            'agents':agents,
            'activities': activities,
            'task':task
        }
        return render(request,'tasks/edit-task.html',dic)

    def post(self,request):
        task = get_object_or_404(Task,pk=request.POST['task'])
        print task
        agent = get_object_or_404(Agent,pk=request.POST['agent'])
        activity = get_object_or_404(Activity,pk=request.POST['activity'])
        toDo = request.POST['toDo']
        startTime = request.POST['startTime']
        endTime = request.POST['endTime']
        comment = request.POST['comment']
        user = get_object_or_404(User,pk=request.user.id)

        task.date_to_do = toDo
        task.start_time = startTime
        task.end_time = endTime
        task.comment = comment
        task.agent = agent
        task.activity = activity
        task.user = user
        task.created = task.created

        task.save()

        return redirect('/tasks/list/')

class TaskDeleteView(View):

    def get(self,request,id):
        task = get_object_or_404(Task,pk=id)
        task.delete()
        return redirect('/tasks/list/')
