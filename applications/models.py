from django.db import models

class ApplicationArea( models.Model ):
	title = models.CharField( max_length = 50 )
	desc = models.TextField()
	img = models.CharField( max_length = 60 )
