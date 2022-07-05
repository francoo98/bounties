from django.urls import path

from .views import api_bounty_list, api_bounty_detail 

app_name = 'bounties_api'

urlpatterns = [
    path('', api_bounty_list, name='bounties_list'),
    path('<int:pk>', api_bounty_detail, name='bounty_detail'),
]
