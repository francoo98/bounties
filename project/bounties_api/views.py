from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework import viewsets


from bounties.models import Bounty, Solution
from .serializers import BountySerializer, SolutionSerializer
from .permissions import IsOwnerOrReadOnly

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

