from rest_framework import serializers
from .models import Bounty


class BountySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bounty
        fields = ['id', 'title', 'description', 'reward',
                  'creation_date', 'creator', 'status', 'awarded_solution']

    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=40)
    description = serializers.CharField(max_length=100)
    reward = serializers.IntegerField()

    def create(self, validated_data):
        return Bounty.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.reward = validated_data.get('reward', instance.reward)
        instance.save()
        return instance
        """
