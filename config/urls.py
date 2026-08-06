print("CONFIG URLS LOADED")
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Smart Task Manager API",
        default_version="v1",
        description="API Documentation for Smart Task Manager",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Authentication APIs
    path("api/auth/", include("apps.accounts.urls")),

    # Project APIs
    path("api/projects/", include("apps.projects.urls")),

    # Task APIs
    path("api/tasks/", include("apps.tasks.urls")),

    # Swagger Documentation
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    # ReDoc Documentation
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]