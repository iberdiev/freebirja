from django.urls import path
from . import views
from .models import User
urlpatterns = [
    path('', views.HomePage, name = 'home'),
    path('login', views.LogInPage.as_view(), name = 'login'),
    path('signup', views.SignUpPage, name='signup'),
    path('employeeslist', views.EmployeesList, name='eelist'),
    path('employerslist', views.EmployersList, name='erlist'),
    path('tasks', views.tasks_list, name='tasks'),
    path('taskcreate', views.TaskCreateView, name='create_task'),
    path('tasks/money-transfer', views.MoneyTransfer, name='money_transfer')
]
