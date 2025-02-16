from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),

    path("api/", include([
        path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
        path("staff/", include("staff.urls")),
        path("news/", include("news.urls")),
        path("", include("study.urls")),
    ])),
]

