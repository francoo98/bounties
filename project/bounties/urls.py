from django.urls import path
from .views import RecentBounties

urlpatterns = [
    path('', RecentBounties.as_view(), name="recent_bounties"),
]
