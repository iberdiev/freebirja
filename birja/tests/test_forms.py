from django.test import TestCase
from birja.forms import SignUpForm, TaskCreateForm

class TaskCreateFormTest(TestCase):
    form = TaskCreateForm()

    def test_data_in_past(self):
        form_data = {'name': 'task1',
                     'description': 'task1 description',
                     'cost':10}
        form = TaskCreateForm(data = form_data)
        self.assertTrue(form.is_valid())

#fields = ('name', 'description', 'cost')
