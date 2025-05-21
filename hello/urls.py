from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.index, name="index"),
    path("add/", views.two, name="two"),
    path("<str:name>/", views.greet, name="greet")
]