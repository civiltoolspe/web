from django.urls import path
from . import views

app_name = "calculators"
urlpatterns = [
    path("", views.index, name="index"),
    path("canal-rectangular/", views.canal_rectangular, name="canal_rectangular"),
]
