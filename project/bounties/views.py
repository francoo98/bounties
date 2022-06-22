from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from bounties.models import Bounty

class RecentBounties(generic.ListView):
    template_name = 'bounties/index.html'
    context_object_name = 'bounties_list'

    def get_queryset(self):
        return Bounty.objects.all()

class ViewBounty(generic.DetailView):
    model = Bounty 
    template_name = 'bounties/view_bounty.html'

class DeleteBounty(generic.DeleteView):
    model = Bounty
    success_url = reverse_lazy('bounties:recent_bounties')

class CreateBounty(LoginRequiredMixin, generic.CreateView):
    model = Bounty
    fields = ['title', 'description', 'reward']
    template_name = 'bounties/create_bounty.html'

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # creator = request.user
            new_bounty = Bounty(title=request.POST["title"], description=request.POST["description"], reward=request.POST["reward"], creator=request.user)
            new_bounty.save()
            return redirect(new_bounty)
