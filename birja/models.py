from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
class UserManager(BaseUserManager):

    def create_user(self, username, password=None, balance=0, is_staff=False, is_admin=False, is_active=True):
        if not username:
            raise ValueError("Users must have username")
        if not password:
            raise ValueError("Users must have password")
        user_obj = self.model(
            username = self.normalize_email(username)
        )
        user_obj.set_password(password)
        user_obj.balance = balance
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, username, password=None):
        user = self.create_user(
                username,
                password = password,
                is_staff = True
        )

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff = True,
            is_admin = True,
        )
        return user


class User(AbstractBaseUser):
    EMPLOYER = 1
    EMPLOYEE = 2
    ROLE_CHOICES = (
        (EMPLOYER, 'Employer'),
        (EMPLOYEE, 'Employee'),
    )
    username = models.CharField(max_length = 20, unique=True)
    USERNAME_FIELD = 'username'
    balance = models.IntegerField()
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    #username and password are required by default, and balance is optional, if it's not set, the it's zero by default
    objects = UserManager()


    def __str__(self):
        # return '%s %s %s' % (self.username, self.role, self.balance)
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date_published', auto_now_add = True)
    cost = models.IntegerField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    OPENNED = 1
    CLOSED = 0
    ROLE_CHOICES = (
        (OPENNED, 'Openned'),
        (CLOSED, 'Closed'),
    )
    status = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True, default = 1)
    def __str__(self):
        return '%s' % (self.name)
