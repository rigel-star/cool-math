from django.shortcuts import render
from django.http import HttpResponse
from .models import HomeContent, FactContent

def index_func( request ):
	conts = [
		HomeContent("./prime", "Prime World", "Get to know about prime numbers..."),
		HomeContent("./geom", "Geometry", "Explore world of shapes..."),
		HomeContent( "./applications",
				"Applications", "Know where math is being used in real world." ),
		HomeContent( "./expreval", "Evaluate Expressions", "Evaluate algebric expressions.")
		]

	dct = { "contents":conts, "fact":FactContent( "Square Numbers",
		"Take a & b which are squares where a > b, then a - b is also a square." ) }

	return render( request, "index.html", dct )

def about_func( request ):
	return HttpResponse( "<h1>About me</h1>" )
