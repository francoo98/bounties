from rest_framework import serializers
from bounties.models import Bounty, Solution
from django.contrib.auth.models import User


class BountySerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Bounty
        fields = ['id', 'title', 'description', 'reward',
                  'creation_date', 'creator', 'status', 'awarded_solution']

class SolutionSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Solution
        fields = ['id', 'bounty', 'status', 'text', 'creator']