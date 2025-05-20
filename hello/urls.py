from django.urls import path
from . import views
urlpatterns = [
    path("test/", views.index, name="index"),
    path("add/", views.two, name="two")
]