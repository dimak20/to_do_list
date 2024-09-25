from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('management:tag-detail', args=[str(self.id)])


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('management:task-detail', args=[str(self.id)])

    @property
    def is_done(self):
        return self.status
