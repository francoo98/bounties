from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from bounties.models import Bounty

class RecentBounties(generic.ListView):
    template_name = 'bounties/index.html'
    context_object_name = 'bounties_list'

    def get_queryset(self):
        return [1,2,3]

def create_bounty(request):
    if request.method == 'GET':
        return render(request, 'bounties/create_bounty.html')
    if request.method == 'POST':
        new_bounty = Bounty(title = request.POST["title"], description = request.POST["description"], reward = request.POST["reward"])
        new_bounty.save()
        return HttpResponse("Bounty created")