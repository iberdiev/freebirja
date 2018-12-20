from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Task
from django.db import models


User = get_user_model()

class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'balance', 'is_admin', 'role')

    search_fields = ['username','role']
    class Meta:
        model = User

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'pub_date', 'cost','author', 'status')
    class Meta:
        model = Task

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)





# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
