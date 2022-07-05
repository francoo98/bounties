from rest_framework import serializers
from bounties.models import Bounty


class BountySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bounty
        fields = ['id', 'title', 'description', 'reward',
                  'creation_date', 'creator', 'status', 'awarded_solution']
