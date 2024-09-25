from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from to_do_management.models import Task, Tag


class ModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), tag.name)

    def test_task_str(self):
        task = Task.objects.create(
            content="test",
            created_time=timezone.now(),
            deadline=timezone.now() + timedelta(days=1)
        )
        self.assertEqual(
            str(task), (
                f"{task.content} "
                f"{task.created_time} "
                f"{task.deadline}"
            )
        )

