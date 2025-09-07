from django.urls import path
from . import views

app_name = "templates_store"
urlpatterns = [
    path("", views.index, name="index"),
]
