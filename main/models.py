from django.db import models

class HomeContent():
	link = ''
	title = ''
	desc = ''
	
	def __init__( self, link, title, desc ):
		self.link = link
		self.title = title
		self.desc = desc
		

class FactContent():
	title = ''
	desc = ''
	
	def __init__( self, title, desc ):
		self.title = title
		self.desc = desc
