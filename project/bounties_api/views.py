from rest_framework import generics, permissions, status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


from bounties.models import Bounty, Solution
from .serializers import BountySerializer, SolutionSerializer
from .permissions import IsOwnerOrReadOnly


"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users_api:users_list', request=request, format=format),
        'bounties': reverse('bounties_list', request=request, format=format)
    })
"""

class BountyViewSet(viewsets.ModelViewSet):
    queryset = Bounty.objects.all()
    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Bounty.DELETED
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Solution.DELETED
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BountyList(generics.ListCreateAPIView):
    """
    List all bounties (GET) or create a new one (POST)
    """

    queryset = Bounty.objects.all()
    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class BountyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Bounty instance
    """

    queryset = Bounty.objects.all()
    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_destroy(self, bounty):
        bounty.status = Bounty.DELETED
        bounty.save()
