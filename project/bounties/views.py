from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from bounties.models import Bounty, Solution


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


class DeleteSolution(DeleteView):
    model = Solution
    success_url = reverse_lazy('bounties:recent_bounties')

    def form_valid(self, form):
        success_url = reverse_lazy('bounties:view_bounty', args=(self.kwargs['bounty_pk'],))
        self.object.status = Solution.DELETED
        self.object.save()
        return HttpResponseRedirect(success_url)

    def test_func(self):
        solution = self.model.objects.get(id=self.kwargs['pk'])
        return self.request.user == solution.creator
