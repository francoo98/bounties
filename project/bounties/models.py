from django.db import models
from django.utils import timezone

class Bounty(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    reward = models.PositiveSmallIntegerField()
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(reward__range=(1, 500)), name='reward_range'),
        ]