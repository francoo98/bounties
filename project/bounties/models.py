from django.db import models
from django.utils import timezone
from django.urls import reverse

class Bounty(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    reward = models.PositiveSmallIntegerField()
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(reward__range=(1, 500)), name='reward_range'),
        ]
    
    def get_absolute_url(self):
        return reverse('bounties:view_bounty', kwargs={'pk' : self.id})

    def __str__(self):
        return self.title