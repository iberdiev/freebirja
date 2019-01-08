from django.test import TestCase
from birja.models import Task, User

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(username='iskender', balance = 111)

    def test_first_name_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'username')

    def test_balance_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('balance').verbose_name
        self.assertEquals(field_label, 'balance')

    def test_first_name_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length,20)

    def test_active_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('active').verbose_name
        self.assertEquals(field_label,'active')

    def test_staff_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('staff').verbose_name
        self.assertEquals(field_label,'staff')

    def test_admin_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('admin').verbose_name
        self.assertEquals(field_label,'admin')

    def test_role_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('role').verbose_name
        self.assertEquals(field_label,'role')

    def test_username_value(self):
        user=User.objects.get(id=1)
        value = user.username
        self.assertEquals(value, 'iskender')

    def test_balance_value(self):
        user=User.objects.get(id=1)
        value = user.balance
        self.assertEquals(value, 111)

    def test_active_value(self):
        user=User.objects.get(id=1)
        value = user.active
        self.assertEquals(value, True)

    def test_staff_value(self):
        user=User.objects.get(id=1)
        value = user.staff
        self.assertEquals(value, False)

    def test_admin_value(self):
        user=User.objects.get(id=1)
        value = user.admin
        self.assertEquals(value, False)

    def test_role_value(self):
        user=User.objects.get(id=1)
        value = user.role
        self.assertEquals(value, None)

    def test_object_name(self):
        user=User.objects.get(id=1)
        expected_object_name = user.username
        self.assertEquals(expected_object_name, str(user))


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Task.objects.create(name='task',
                            description='task description',
                            cost = 10,
                            pub_date = 'test data'
        )

    def test_name_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_pub_date_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('pub_date').verbose_name
        self.assertEquals(field_label,'date_published')

    def test_cost_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('cost').verbose_name
        self.assertEquals(field_label,'cost')

    def test_author_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('author').verbose_name
        self.assertEquals(field_label,'author')

    def test_status_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_name_value(self):
        task = Task.objects.get(id=1)
        value = task.name
        self.assertEquals(value, 'task')

    def test_description_value(self):
        task = Task.objects.get(id=1)
        value = task.description
        self.assertEquals(value, 'task description')

    def test_cost_value(self):
        task = Task.objects.get(id=1)
        value = task.cost
        self.assertEquals(value, 10)

    def test_author_value(self):
        task = Task.objects.get(id=1)
        value = task.author
        self.assertEquals(value, None)

    def test_status_value(self):
        task = Task.objects.get(id=1)
        value = task.status
        self.assertEquals(value, 1)

    def test_object_name(self):
        task=Task.objects.get(id=1)
        expected_object_name = task.name
        self.assertEquals(expected_object_name, str(task))
