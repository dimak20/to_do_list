from http.client import HTTPResponse

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_management.forms import TaskForm, TaskSearch
from to_do_management.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "to_do_management/home2.html"

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags")

        sort_by = self.request.GET.get("sort_by", "id")
        sort_dir = self.request.GET.get("sort_dir", "asc")
        sort_order = "" if sort_dir == "asc" else "-"

        if sort_by == "status":
            queryset = queryset.order_by(f"{sort_order}status")

        else:
            queryset = queryset.order_by(f"{sort_order}{sort_by}")

        form = TaskSearch(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                content__icontains=form.cleaned_data["content"]
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_sort_by"] = self.request.GET.get("sort_by", "id")
        context["current_sort_dir"] = self.request.GET.get("sort_dir", "asc")
        content = self.request.GET.get("content", "")
        context["search_form"] = TaskSearch(
            initial={"content": content}
        )
        return context


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


class UserListView(generic.ListView):
    model = get_user_model()
    template_name = "to_do_management/user_list.html"
