from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bounties.models import Bounty
from .serializers import BountySerializer


@api_view(['GET', 'POST'])
def api_bounty_list(request, format=None):
    """
    List all bounties, or create a new bounty.
    """
    if request.method == 'GET':
        bounties = Bounty.objects.all()
        serializer = BountySerializer(bounties, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = BountySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_bounty_detail(request, pk, format=None):
    bounty = get_object_or_404(Bounty, id=pk)

    if request.method == 'GET':
        serializer = BountySerializer(bounty)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = BountySerializer(bounty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bounty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
