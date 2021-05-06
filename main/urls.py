from django.urls import path, include

from . import views

urlpatterns = [
    path( '', views.index_func, name="home" ),
    path( 'about/', views.about_func, name="about" )
]
