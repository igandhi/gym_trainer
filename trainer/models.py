import uuid
from django.db import models
from django.utils import timezone

class Routine(models.Model):
    routine_name = models.CharField(max_length=50)
    random_url = models.UUIDField(default=uuid.uuid4)
    created_timestamp = models.DateTimeField(default=timezone.now)

class Exercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
