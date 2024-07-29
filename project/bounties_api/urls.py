from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BountyViewSet, SolutionViewSet

app_name = 'bounties_api'

router = DefaultRouter()
router.register(r'bounties', BountyViewSet, basename='bounties')
router.register(r'solution', SolutionViewSet, basename='solutions')

urlpatterns = [
    path('', include(router.urls)),
]
