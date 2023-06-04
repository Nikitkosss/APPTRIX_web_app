from rest_framework import filters, viewsets

from api.models import Coin, News
from api.permissions import AuthenticatedPrivilegedUsersOrReadOnly
from api.serializers import CoinSerializer, NewsSerializer


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = (AuthenticatedPrivilegedUsersOrReadOnly,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'code')
    lookup_field = 'code'


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AuthenticatedPrivilegedUsersOrReadOnly,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('author', 'description', 'title')
