from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Specialization, Course
from .permissions import ReadOnly
from .serializers import SpecializationSerializer, CourseSerializer

class SpecializationListView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = "id title term contract".split()
    search_fields = "id title term contract".split()
    ordering_fields = "id title contract".split()


class SpecializationDetailView(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [ReadOnly]

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = SpecializationSerializer

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = "id title term price".split()
    search_fields = "id title term price".split()
    ordering_fields = "id title price".split()

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [ReadOnly]