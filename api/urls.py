from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
    path("melon/", views.melon_list, name="melon_list"),
]
