from django.urls import path

from .views import SpecializationListView, SpecializationDetailView, CourseListView, CourseDetailView

urlpatterns = [
    path("specialization/", SpecializationListView.as_view(), name="specialization-list"),
    path("specialization/<int:pk>/", SpecializationDetailView.as_view(), name="specialization-detail"),

    path("course/", CourseListView.as_view(), name="course-list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
]
