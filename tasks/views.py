from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
# my models
from agents.models import Agent
from activities.models import Activity
from .models import Task
from files.models import File

#utilities
from datetime import date

def send_response_to_supervisor(self,first_name,last_name,id,status,user_email):
    send_mail(
    'Tarea de %s %s' %(first_name,last_name),
    "La solicitud con numero %s del agente %s %s fue %s" %(id,first_name,last_name,status),
     "wfm@idealccs.com",
      [user_email],
       fail_silently=True)


class TemplateView(View):

    def get(self,request):
        if request.user.is_staff:
            tasks = Task.objects.filter(status='pendiente').order_by('created')
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
        activities = Activity.objects.all()
        users = User.objects.all()
        dic = {
            'tasks':advancedSearch(request),
            'activities':activities,
            'users': users,
        }
        return render(request,'tasks/index.html',dic)


class CreateTaskView(View):

    def get(self,request):
        user = User.objects.get(id=request.user.id)
        agents = Agent.objects.filter(user__id = user.id).filter(status="Activo")
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

        )
        task.save()
        if request.FILES:
            restriction_file = request.FILES['restrictionFile']
            evidence_file = request.FILES['evidenceFile']
            restriction_file_object = File(document = restriction_file)
            restriction_file_object.save()
            evidence_file_object = File(document = evidence_file)
            evidence_file_object.save()
            task.document.add(restriction_file_object)
            task.document.add(evidence_file_object)

        return redirect('/tasks/list/')

class TaskDetailView(View):

    def get(self,request,id):
        task = get_object_or_404(Task,pk=id)
        dic = {
            'task':task
        }
        return render(request,'tasks/detail-task.html',dic)

class AproveView(View):

    def get(self,request,id):
        task = get_object_or_404(Task,pk=id)
        user_email = task.user.email
        task.status = 'aprobado'
        task.save()
        send_response_to_supervisor(self,task.agent.first_name,task.agent.last_name,task.id,task.status,user_email)
        return redirect('/tasks/')

class DeclineView(View):

    def get(self,request,id):
        task = get_object_or_404(Task,pk=id)
        user_email = task.user.email
        task.status = 'rechazada'
        task.save()
        send_response_to_supervisor(self,task.agent.first_name,task.agent.last_name,task.id,task.status,user_email)
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
        agents = Agent.objects.filter(user__id = user.id).filter(status="Activo")
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


def advancedSearch(request):
    status = request.POST.get('status')
    activity = request.POST.get('activity')
    supervisor = request.POST.get('user')
    date = request.POST.get('date')
    print status
    print activity
    if status != "0":
        results = Task.objects.filter(status=status).order_by('-created')
    else:
        results = Task.objects.all().order_by('-created')
        print results
    if activity != "0":
        results = results.filter(activity_id=activity)
    if supervisor != "0":
        results = results.filter(user_id = supervisor)
    if date != "":
        results = results.filter(created=date)
        print date



    return results
