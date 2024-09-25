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

    def test_retrieve_tasks(self):
        tasks = [
            Task(
                content=f"test_{i}",
                created_time=timezone.now(),
                deadline=timezone.now() + timedelta(days=1)
            ) for i in range(8)
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

    def test_delete_task(self):
        task_id = self.task.id
        response = self.client.post(reverse("management:task-delete", args=[task_id]))
        self.assertEqual(response.status_code, 302)
        deleted_task = Task.objects.filter(id=task_id).exists()
        self.assertFalse(deleted_task)

    def test_pagination_task(self):
        tasks = [
            Task(
                content=f"test_pagination{i}",
                created_time=timezone.now(),
                deadline=timezone.now() + timedelta(days=1)
            ) for i in range(20)
        ]
        Task.objects.bulk_create(tasks)
        response = self.client.get(TASK_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()[:10]
        self.assertEqual(list(response.context["task_list"]), list(tasks))
        self.assertTemplateUsed(response, "to_do_management/home2.html")


class PrivateTagTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test123", password="test1234"
        )
        self.client.force_login(self.user)
        self.tag = Tag.objects.create(name="test_name_1")
        self.task = Task.objects.create(
            content=f"test_mmm",
            created_time=timezone.now(),
            deadline=timezone.now() + timedelta(days=1)
        )

    def test_retrieve_tags(self):
        tags = [
            Tag(
                name=f"tag_test_name_{i}",
            ) for i in range(5)
        ]
        Tag.objects.bulk_create(tags)
        response = self.client.get(TAG_URL)
        self.assertEqual(response.status_code, 200)
        tags = Tag.objects.all()
        self.assertEqual(list(response.context["tag_list"]), list(tags))
        self.assertTemplateUsed(response, "to_do_management/tag_list.html")

    def test_create_tag(self):
        payload = {
            "name": "new_unique_name",
        }
        response = self.client.post(reverse("management:tag-create"), data=payload)
        self.assertEqual(response.status_code, 302)
        task = Tag.objects.filter(name="new_unique_name").exists()
        self.assertTrue(task)

    def test_update_tag(self):
        payload = {
            "name": "new_unique_payload",
        }
        response = self.client.post(reverse("management:tag-update", args=[self.tag.id]), data=payload)
        tag = Tag.objects.get(id=self.tag.id)
        tag.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(tag.name, payload["name"])

    def test_delete_tag(self):
        tag_id = self.tag.id
        response = self.client.post(reverse("management:tag-delete", args=[tag_id]))
        self.assertEqual(response.status_code, 302)
        deleted_tag = Tag.objects.filter(id=tag_id).exists()
        self.assertFalse(deleted_tag)
