from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.openapi import AutoSchema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Staff
from common.permissions import ReadOnly
from .serializers import StaffSerializer

class StaffListView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = "id name position phone_number email".split()
    search_fields = "id name position email".split()
    ordering_fields = "id name position".split()



class StaffDetailView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]