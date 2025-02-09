from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Staff
from common.permissions import ReadOnly
from .serializers import StaffSerializer

class StaffListView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = "id name position phone_number email".split()
    search_fields = "id name position email".split()
    ordering_fields = "id name position".split()



class StaffDetailView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [ReadOnly]