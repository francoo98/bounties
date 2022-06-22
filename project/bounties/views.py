from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

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

def create_bounty(request):
    if request.method == 'GET':
        return render(request, 'bounties/create_bounty.html')
    if request.method == 'POST':
        new_bounty = Bounty(title = request.POST["title"], description = request.POST["description"], reward = request.POST["reward"])
        new_bounty.save()
        return redirect(new_bounty)