from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("homepage.urls", "homepage"), namespace="homepage")),
    path("", include(("catalog.urls", "catalog"), namespace="catalog")),
    path("", include(("about.urls", "about"), namespace="about")),
    path("", include(("feedback.urls", "feedback"), namespace="feedback")),
    path("summernote/", include("django_summernote.urls")),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
