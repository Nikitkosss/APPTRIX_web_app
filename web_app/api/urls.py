from django.urls import include, path
from rest_framework import routers

from api.views import CoinViewSet, NewsViewSet

v1_router = routers.DefaultRouter()
v1_router.register('coins', CoinViewSet)
v1_router.register('news', NewsViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
