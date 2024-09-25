from django.contrib import admin

from to_do_management.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
