from django.urls import path
from .views import RecentBounties, create_bounty

app_name = 'bounties'

urlpatterns = [
    path('', RecentBounties.as_view(), name="recent_bounties"),
    path('create/', create_bounty, name="create_bounty"),
]
