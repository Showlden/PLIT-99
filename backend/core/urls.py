from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as get_swagger_view

schema_view = get_swagger_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),

    path("api/", include([
        path("staff/", include("staff.urls")),  # Correct way to include
        path("news/", include("news.urls")),  # Correct way to include
        path("", include("study.urls")),  # Correct way to include
    ])),
]
