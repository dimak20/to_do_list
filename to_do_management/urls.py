from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from to_do_management.views import index

app_name = "management"

urlpatterns = [
    path("", index, name="index"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)