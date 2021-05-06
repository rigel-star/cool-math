from django.urls import path

from . import views

urlpatterns = [
    path( '', views.expreval_home, name="home" )
]
