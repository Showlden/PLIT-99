from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as get_swagger_view

schema_view = get_swagger_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),

    path("staff/", include("staff.urls"))
]
