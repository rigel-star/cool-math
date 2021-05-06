from django.urls import path
from . import views

urlpatterns = [
	path( '', views.applications_home, name="home" ),
	path( 'desc/', views.read_app_desc, name="desc" )
]
