from django.db import models

PRIORITIES = (
    ("high", "Priority High"),
    ("medium", "Priority Medium"),
    ("low", "Priority Low"),
)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITIES, default="low")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
