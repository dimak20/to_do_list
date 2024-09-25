from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do_management.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "to_do_management/home.html"

class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "to_do_management/task_form.html"
    success_url = reverse_lazy("management:home")
