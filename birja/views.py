from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task
from .forms import SignUpForm, TaskCreateForm
from . import models
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test, login_required


def HomePage(request):
    info = User.objects.all()
    return render(request, 'birja/home.html', {'info':info})


class LogInPage(TemplateView):
    template_name = 'registration/login.html'

def SignUpPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def EmployeesList(request):
    list = User.objects.all().filter(role=2)
    return render(request, 'employer/employees_list.html',{'list':list})


def EmployersList(request):
    list = User.objects.all().filter(role=1)
    return render(request, 'employee/employers_list.html',{'list':list})

def employee_check(User):
    return User.role==2
@user_passes_test(employee_check)
def tasks_list(request):
    tasks = Task.objects.all().filter(status=1)
    return render(request, 'employee/tasks.html', {'tasks':tasks} )

def employer_check(User):
    return User.role==1

@login_required
@user_passes_test(employer_check)
def TaskCreateView(request):

    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save().author = request.user
            form.save()
            return redirect('home')
    else:
        form = TaskCreateForm()
    return render(request, 'employer/create_task.html', {'form': form})

@transaction.atomic
def MoneyTransfer(request):

    task_name = request.POST.get('task')
    task = Task.objects.select_for_update().get(name=task_name)
    task_cost = task.cost
    # task_cost = task_name.cost
    task_author = task.author

    author = User.objects.select_for_update().get(username=task_author)
    if author.balance >= task_cost:

        author.balance -= task_cost
        author.save()
        employee = User.objects.select_for_update().get(username=request.user)
        employee.balance += task_cost
        employee.save()
        validity = True
        task.status = 0
        task.save
    else:
        validity = False
    task.save()
    return render(request, 'employee/money_transfer.html', {'validity':validity, 'task_name':task_name, 'task_cost':task_cost, 'task_author':task_author})
