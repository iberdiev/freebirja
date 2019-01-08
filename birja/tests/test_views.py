from django.test import TestCase
# from birja.views import
from birja.models import User, Task

class EmployersListViewTest(TestCase):
    @classmethod
    def setUp(cls):
        number_of_employers = 10
        for num in range(number_of_employers):
            User.objects.create(username='Employer %s' % num,
            balance = 10,
            role = 1,
            password = 123
            )

    def test_view_url_exists(self):
        resp = self.client.get('/employerslist')
        self.assertEqual(resp.status_code, 200)

    def test_lists_all_employers(self):
        resp = self.client.get('/employerslist')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue( len(resp.context['list']) == 10)

class EmployeesListViewTest(TestCase):
    @classmethod
    def setUp(cls):
        number_of_employees = 10
        for num in range(number_of_employees):
            User.objects.create(username='Employee %s' % num,
            balance = 10,
            role = 2,
            password = 123
            )

    def test_view_url_exists(self):
        resp = self.client.get('/employeeslist')
        self.assertEqual(resp.status_code, 200)

    def test_lists_all_employees(self):
        resp = self.client.get('/employeeslist')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue( len(resp.context['list']) == 10)

class TaskCreateViewTest(TestCase):
    @classmethod
    def setUp(self):
        test_user = User.objects.create(username='employer',
        balance = 10,
        role = 1,
        )
        test_user.set_password('123')
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get('/taskcreate')
        self.assertRedirects(resp, '/accounts/login/?next=/taskcreate')

    def test_redirect_if_logged_in(self):
        login = self.client.login(username='employer', password = '123')
        resp = self.client.get('/taskcreate')
        self.assertEqual(str(resp.context['user']), 'employer')
        self.assertEqual(resp.status_code, 200)

class MoneyTransferTest(TestCase):

    @classmethod
    def setUp(self):
        test_user1 = User.objects.create(username='employer1',
        balance = 10,
        role = 1,
        )
        test_user1.set_password('123')
        test_user1.save()

        test_user2 = User.objects.create(username='employee1',
        balance = 10,
        role = 2,
        )
        test_user2.set_password('123')
        test_user2.save()
        task = Task.objects.create(name='task',
                            description='task description',
                            cost = 1,
                            pub_date = 'test data',
                            author = User.objects.get(id=1)
        )
        task.save()

    def test_money_transfer(self):
        task = Task.objects.get(id=1)
        self.assertEquals(task.status, 1)
        self.assertEquals(task.cost, 1)
        employer = User.objects.get(id=1)
        employee = User.objects.get(id=2)
        self.assertEquals(employer.balance, 10)
        self.assertEquals(employee.balance, 10)

        login = self.client.login(username='employee1', password = '123')
        resp = self.client.get('/tasks')
        self.assertEqual(str(resp.context['user']), 'employee1')
        self.assertEqual(resp.status_code, 200)

        if employer.balance >= task.cost:
            employer.balance -= task.cost
            employer.save()
            employee.balance += task.cost
            employee.save()
            task.status = 0
            task.save()

        self.assertEquals(task.status, 0)
        self.assertEquals(employer.balance, 9)
        self.assertEquals(employee.balance, 11)
