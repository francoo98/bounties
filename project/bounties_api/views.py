from rest_framework import generics

from bounties.models import Bounty
from .serializers import BountySerializer


class BountyList(generics.ListCreateAPIView):
    """
    List all bounties (GET) or create a new one (POST)
    """

    queryset = Bounty.objects.all()
    serializer_class = BountySerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class BountyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Bounty instance
    """

    queryset = Bounty.objects.all()
    serializer_class = BountySerializer
