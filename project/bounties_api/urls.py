from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BountyViewSet, SolutionViewSet

app_name = 'bounties_api'

router = DefaultRouter()
router.register(r'bounty', BountyViewSet, basename='bounties')
router.register(r'solution', SolutionViewSet, basename='solutions')

urlpatterns = [
    path('', include(router.urls)),
]

"""
urlpatterns = [
    path('', BountyList.as_view(), name='bounties_list'),
    path('<int:pk>', BountyDetail.as_view(), name='bounty_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
"""
