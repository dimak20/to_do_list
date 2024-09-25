from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from to_do_management.forms import TaskForm, TaskSearch
from to_do_management.models import Task


class TaskSearchFormTests(TestCase):
    def setUp(self):
        self.tasks = [
            Task(
                content=f"test_{i}",
                created_time=timezone.now(),
                deadline=timezone.now() + timedelta(days=1)
            ) for i in range(20)
        ]
        Task.objects.bulk_create(self.tasks)

    def test_form_valid_data(self):
        form = TaskSearch(data={"content": "1"})
        self.assertTrue(form.is_valid())
        content = form.cleaned_data["content"]
        tasks = Task.objects.filter(content__icontains=content)
        self.assertEqual(tasks.count(), 11)
        self.assertEqual(tasks.first().content, "test_1")

    def test_form_invalid_data(self):
        form = TaskSearch(data={"content": "NonExistent"})
        self.assertTrue(form.is_valid())
        content = form.cleaned_data["content"]
        tasks = Task.objects.filter(content__icontains=content)
        self.assertEqual(tasks.count(), 0)


class TaskFormTests(TestCase):
    def setUp(self):
        self.tasks = [
            Task(
                content=f"test_{i}",
                created_time=timezone.now(),
                deadline=timezone.now() + timedelta(days=1)
            ) for i in range(5)
        ]

    def test_form_valid_data(self):
        form = TaskForm(
            data={
                "content": "test_content",
                "created_time": timezone.now(),
                "deadline": timezone.now() + timedelta(days=1)

            }
        )
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = TaskForm(
            data={
                "content": "test_content",
                "created_time": timezone.now(),
                "deadline": timezone.now() - timedelta(days=1)
            }
        )
        self.assertFalse(form.is_valid())
