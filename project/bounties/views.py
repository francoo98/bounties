from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied, BadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bounties.models import Bounty, Solution
from bounties.serializers import BountySerializer


class RecentBounties(ListView):
    template_name = 'bounties/index.html'
    context_object_name = 'bounties_list'

    def get_queryset(self):
        return Bounty.objects.exclude(status=Bounty.DELETED)


class ViewBounty(DetailView):
    model = Bounty
    template_name = 'bounties/view_bounty.html'


class DeleteBounty(UserPassesTestMixin, DeleteView):
    model = Bounty
    success_url = reverse_lazy('bounties:recent_bounties')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = Bounty.DELETED
        self.object.save()
        return HttpResponseRedirect(success_url)

    def test_func(self):
        bounty = self.model.objects.get(id=self.kwargs['pk'])
        return self.request.user == bounty.creator


class CreateBounty(LoginRequiredMixin, CreateView):
    model = Bounty
    fields = ['title', 'description', 'reward']
    template_name = 'bounties/create_bounty.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class CreateSolution(LoginRequiredMixin, CreateView):
    model = Solution
    fields = ['text']

    def form_valid(self, form):
        bounty = Bounty.objects.get(id=self.kwargs['pk'])
        form.instance.bounty = bounty
        form.instance.creator = self.request.user
        self.success_url = reverse_lazy(
            'bounties:view_bounty', args=(self.kwargs['pk'],))
        return super().form_valid(form)


class DeleteSolution(UserPassesTestMixin, DeleteView):
    model = Solution
    success_url = reverse_lazy('bounties:recent_bounties')

    def form_valid(self, form):
        success_url = reverse_lazy(
            'bounties:view_bounty', args=(self.kwargs['bounty_pk'],))
        self.object.status = Solution.DELETED
        self.object.save()
        return HttpResponseRedirect(success_url)

    def test_func(self):
        solution = self.model.objects.get(id=self.kwargs['pk'])
        return self.request.user == solution.creator


def award_solution(request, bounty_pk, pk):
    bounty = get_object_or_404(Bounty, pk=bounty_pk)
    solution = get_object_or_404(Solution, pk=pk)

    if not request.user.is_authenticated or request.user != bounty.creator:
        raise PermissionDenied
    if request.method != 'GET':
        raise BadRequest

    bounty.awarded_solution = solution
    solution.status = Solution.AWARDED
    bounty.save()
    solution.save()

    return redirect(bounty, reverse('bounties:view_bounty', args=(bounty_pk,)))


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
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BountySerializer(bounty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bounty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
