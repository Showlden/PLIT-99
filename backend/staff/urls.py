from django.urls import path

from .views import StaffListView, StaffDetailView

urlpatterns = [
    path("", StaffListView.as_view(), name="staff-list"),
    path("<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
]
