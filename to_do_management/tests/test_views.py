from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from to_do_management.models import Task, Tag

TASK_URL = reverse("management:home")
TAG_URL = reverse("management:tag-list")


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="test123"
        )
        self.client.force_login(self.user)
        self.tag = Tag.objects.create(name="test_name")
        self.task = Task.objects.create(
            content=f"test_mmm",
            created_time=timezone.now(),
            deadline=timezone.now() + timedelta(days=1)
        )

    def test_retrieve_cars(self):
        tasks = [
            Task(
                content=f"test_{i}",
                created_time=timezone.now(),
                deadline=timezone.now() + timedelta(days=1)
            ) for i in range(10)
        ]
        Task.objects.bulk_create(tasks)
        Tag.objects.create(name="test_name_123")
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(response.context["task_list"]), list(tasks))
        self.assertTemplateUsed(response, "to_do_management/home2.html")

    def test_create_task(self):
        payload = {
            "content": "fsdgfvd",
            "created_time": timezone.now(),
            "deadline": timezone.now() + timedelta(days=1)
        }
        response = self.client.post(reverse("management:task-create"), data=payload)
        self.assertEqual(response.status_code, 302)
        task = Task.objects.filter(content="fsdgfvd").exists()
        self.assertTrue(task)

    def test_update_task(self):
        payload = {
            "content": "aaa",
            "deadline": timezone.now() + timedelta(days=1)
        }
        response = self.client.post(reverse("management:task-update", args=[self.task.id]), data=payload)
        task = Task.objects.get(id=self.task.id)
        task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(task.content, payload["content"])

    def test_add_tag(self):
        instant_bool = self.task.is_done
        self.client.get(reverse("management:task-change", args=[self.task.id]))
        self.task.refresh_from_db()
        new_bool = self.task.is_done
        self.assertNotEqual(instant_bool, new_bool)
