from django.urls import path
from .views import (DeleteBounty, RecentBounties, ViewBounty, CreateBounty,
                    CreateSolution, DeleteSolution, award_solution,
                    api_bounty_list, api_bounty_detail)
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'bounties'

urlpatterns = [
    path('', RecentBounties.as_view(), name="recent_bounties"),
    path('<int:pk>', ViewBounty.as_view(), name="view_bounty"),
    path('create', CreateBounty.as_view(), name="create_bounty"),
    path('delete/<int:pk>', DeleteBounty.as_view(), name="delete_bounty"),
    path('<int:pk>/solution/create',
         CreateSolution.as_view(), name="create_solution"),
    path('<int:bounty_pk>/solution/delete/<int:pk>',
         DeleteSolution.as_view(), name="delete_solution"),
    path('<int:bounty_pk>/solution/award/<int:pk>',
          award_solution, name='award_solution'),
     path('api/', api_bounty_list, name='api_recent_bounties'),
     path('api/<int:pk>', api_bounty_detail, name='api_bounty_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
