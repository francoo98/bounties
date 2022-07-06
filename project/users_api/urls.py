from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserDetail, UserList

app_name = 'users_api'

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>', UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
