# e_lecturer/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from core.admin import elec_admin
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('elec-admin/', elec_admin.urls),
    path('', include('core.urls')),

    # ── Serve sw.js from the ROOT of the site ──
    # Service Workers MUST be served from / not /static/
    re_path(r'^sw\.js$', serve, {
        'path':     'sw.js',
        'document_root': os.path.join(settings.BASE_DIR, 'static'),
    }),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
