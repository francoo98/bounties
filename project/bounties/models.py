from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Bounty(models.Model):
    ONGOING = 0
    FINISHED_AWARDED = 1
    FINISHED_EXPIRED = 2
    DELETED = 3
    STATUS_CHOICES = [(ONGOING, 'Ongoing'), (FINISHED_AWARDED, 'Awarded'),
                      (FINISHED_EXPIRED, 'Expired'), (DELETED, 'Deleted')]

    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    reward = models.PositiveSmallIntegerField()
    creation_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(
        User, models.DO_NOTHING, primary_key=False, null=True, related_name='bounties')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=ONGOING)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                reward__range=(1, 500)), name='reward_range'),
        ]

    def get_absolute_url(self):
        return reverse('bounties:view_bounty', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Solution(models.Model):
    AWARDED = 0
    UNAWARDED = 1
    DELETED = 2
    STATUS_CHOICES = [(AWARDED, 'Awarded'), (UNAWARDED,
                                             'Unawarded'), (DELETED, 'Deleted')]

    creator = models.ForeignKey(
        User, models.DO_NOTHING, primary_key=False, related_name='solutions')
    bounty = models.ForeignKey(
        Bounty, models.CASCADE, primary_key=False, related_name='solutions')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=UNAWARDED)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"Solution {self.id} to {self.bounty}"
