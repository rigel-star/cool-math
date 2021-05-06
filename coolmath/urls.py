from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path( '', include( 'main.urls' ) ),
    path( 'prime/', include( 'primecalc.urls' ) ),
    path( 'geom/', include( 'geom.urls' ) ),
    path( 'applications/', include( 'applications.urls' ) ),
    path( 'expreval/', include( 'expreval.urls' ) ),
    path( 'admin/', admin.site.urls ),
]

urlpatterns = urlpatterns + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
