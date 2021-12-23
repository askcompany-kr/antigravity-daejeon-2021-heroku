from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="root.html"), name="root"),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
