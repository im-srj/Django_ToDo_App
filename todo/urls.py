from django.urls import include, path

from . import views

urlpatterns = [
    path("delete/<int:id>/", views.delete, name="delete_task"),
    path("completed/<int:id>/", views.completed, name="completed_task"),
    path("", views.tasks, name="tasks"),
]
