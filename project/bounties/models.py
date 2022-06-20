from django.db import models

class Bounty(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    reward = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(reward__dt=0), name='reward_dt_0'),
        ]