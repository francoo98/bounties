from django.urls import path
from .views import DeleteBounty, RecentBounties, ViewBounty, CreateBounty, CreateSolution, DeleteSolution

app_name = 'bounties'

urlpatterns = [
    path('', RecentBounties.as_view(), name="recent_bounties"),
    path('<int:pk>', ViewBounty.as_view(), name="view_bounty"),
    path('create', CreateBounty.as_view(), name="create_bounty"),
    path('delete/<int:pk>', DeleteBounty.as_view(), name="delete_bounty"),
    path('<int:pk>/solution/create', CreateSolution.as_view(), name="create_solution"),
    path('<int:bounty_pk>/solution/delete/<int:pk>', DeleteSolution.as_view(), name="delete_solution")
]
