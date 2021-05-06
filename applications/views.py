from django.shortcuts import render
from .models import ApplicationArea

#application areas

def applications_home( request ):
	apps = ApplicationArea.objects.all()
	return render( request, "apps_home.html", {"apps": apps} )

def read_app_desc( request ):
	app = ApplicationArea( title="Image Compression", desc="Jibbersish", img="Image Compression.jpeg" )
	return render( request, "read_app_desc.html", {"app":app} )
