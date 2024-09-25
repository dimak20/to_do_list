from http.client import HTTPResponse

from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_management.forms import TaskForm
from to_do_management.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "to_do_management/home2.html"

class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    model = Task
    template_name = "to_do_management/task_form.html"
    success_url = reverse_lazy("management:home")

class TaskDetailView(generic.DetailView):
    model = Task

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return self.get_object().get_absolute_url()

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("management:home")


def change_status(request: HttpRequest, pk: int) -> HTTPResponse:
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return redirect("management:home")

class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10

class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("management:tag-list")

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("management:home")

class TagDetailView(generic.DetailView):
    model = Tag

class TagUpdateView(generic.UpdateView):
    model = Tag

    def get_success_url(self):
        return self.get_object().get_absolute_url()


