from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("calculators/", include("apps.calculators.urls")),
    path("plantillas/", include("apps.templates_store.urls")),
    path("cursos/", include("apps.courses.urls")),
    path("blog/", include("apps.blog.urls")),
    path("recursos/", include("apps.resources.urls")),
    path("comunidad/", include("apps.community.urls")),
]
