from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.openapi import AutoSchema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News
from common.permissions import ReadOnly
from .serializers import NewsSerializer


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = "id title date type ".split()
    search_fields = "id title date type".split()
    ordering_fields = "id title date type ".split()



class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]