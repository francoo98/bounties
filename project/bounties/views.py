from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from bounties.models import Bounty

class RecentBounties(ListView):
    template_name = 'bounties/index.html'
    context_object_name = 'bounties_list'

    def get_queryset(self):
        return Bounty.objects.all()

class ViewBounty(DetailView):
    model = Bounty 
    template_name = 'bounties/view_bounty.html'

class DeleteBounty(DeleteView):
    model = Bounty
    success_url = reverse_lazy('bounties:recent_bounties')

class CreateBounty(LoginRequiredMixin, CreateView):
    model = Bounty
    fields = ['title', 'description', 'reward']
    template_name = 'bounties/create_bounty.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    """
    def post(self, request):
        # form = self.form_class(request.POST)
        if form_valid(self, form):
            # creator = request.user
            new_bounty = Bounty(title=request.POST["title"], description=request.POST["description"], reward=request.POST["reward"], creator=request.user)
            new_bounty.save()
            return redirect(new_bounty)
    """
