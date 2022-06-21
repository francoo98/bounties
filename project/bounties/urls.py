from django.urls import path
from .views import RecentBounties, ViewBounty, create_bounty

app_name = 'bounties'

urlpatterns = [
    path('', RecentBounties.as_view(), name="recent_bounties"),
    path('create/', create_bounty, name="create_bounty"),
    path('bounty/<int:pk>', ViewBounty.as_view(), name="view_bounty"),
]
