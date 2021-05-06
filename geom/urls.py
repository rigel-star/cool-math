from django.urls import path

from . import views

urlpatterns = [
    path( '', views.geom_home, name="home" )
]
