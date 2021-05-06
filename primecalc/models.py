from django.db import models
from django.db.models import Model

class HyperLinkContent(Model):
	link = ''
	title = ''
	desc = ''
	
	def __init__( self, link, title, desc ):
		self.link = link
		self.title = title
		self.desc = desc
