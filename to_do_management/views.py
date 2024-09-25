from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do_management.forms import TaskForm
from to_do_management.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "to_do_management/home.html"

class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    model = Task
    template_name = "to_do_management/task_form.html"
    success_url = reverse_lazy("management:home")

class TaskDetailView(generic.DetailView):
    model = Task





class TagListView(generic.ListView):
    pass

class TagCreateView(generic.CreateView):
    pass

class TagDeleteView(generic.DeleteView):
    pass

class TagDetailView(generic.DetailView):
    pass

class TagUpdateView(generic.UpdateView):
    pass

