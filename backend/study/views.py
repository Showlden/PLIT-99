from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.openapi import AutoSchema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Specialization, Course
from common.permissions import ReadOnly
from .serializers import SpecializationSerializer, CourseSerializer

class SpecializationListView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = "id title term contract".split()
    search_fields = "id title term contract".split()
    ordering_fields = "id title contract".split()


class SpecializationDetailView(RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = "id title term price".split()
    search_fields = "id title term price".split()
    ordering_fields = "id title price".split()

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    schema = AutoSchema()

    permission_classes = [ReadOnly]