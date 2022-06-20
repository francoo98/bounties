from django.shortcuts import render
from django.views import generic

class RecentBounties(generic.ListView):
    template_name = 'bounties/index.html'
    context_object_name = 'bounties_list'

    def get_queryset(self):
        return [1,2,3]