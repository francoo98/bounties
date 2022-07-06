from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BountyDetail, BountyList

app_name = 'bounties_api'

urlpatterns = [
    path('', BountyList.as_view(), name='bounties_list'),
    path('<int:pk>', BountyDetail.as_view(), name='bounty_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
