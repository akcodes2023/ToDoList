from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.contrib.auth import login
#from .forms import UserRegistrationForm

from .models import *
from .forms import *

# Create your views here.
def index(request):
    todolistapp = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'todolistapp':todolistapp, 'form':form} # Context dictionary to put the data in here and pass in on to render function 
    #Below line will return the template specified
    return render(request, 'todolistapp/list.html', context)

def updateTask(request, pk): # pk=primary key to make this view more dynamic by throwing dynamic url path, throwing the pk in the url
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render (request, 'todolistapp/update_todolistapp.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render (request, 'todolistapp/delete.html', context)

