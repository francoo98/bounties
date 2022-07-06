from rest_framework import serializers
from django.contrib.auth.models import User

from bounties.models import Bounty

class UserSerializer(serializers.ModelSerializer):
    bounties = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Bounty.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'bounties']
