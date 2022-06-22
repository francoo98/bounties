from django.urls import path
from .views import DeleteBounty, RecentBounties, ViewBounty, create_bounty

app_name = 'bounties'

urlpatterns = [
    path('', RecentBounties.as_view(), name="recent_bounties"),
    path('<int:pk>', ViewBounty.as_view(), name="view_bounty"),
    path('create', create_bounty, name="create_bounty"),
    path('delete/<int:pk>', DeleteBounty.as_view(), name="delete_bounty"),
]
