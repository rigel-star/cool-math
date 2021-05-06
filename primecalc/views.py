from django.shortcuts import render
from django.http import HttpResponse

from .models import HyperLinkContent

class PrimeNumber():
	
	def __init__( self ):
		pass
	
	#check if number is prime or not	
	def isPrime( self, n ):
		if n == 2 or n == 3:
			return True
		elif n == 4:
			return False
		
		for i in range( 2, n >> 1 ):
			if ( n % i == 0 ):
				return False;
		return True
		
	#get prime at specified position	
	def getPrimeAt( self, pos ):
		if pos < 0:
			return 0
		count = 0
		for idx in range( 2, ( 2 << 16 ) ):
			if self.isPrime( idx ):
				count += 1
			if count == pos + 1:
				return idx
		return 0
		
	def getPrimes( self, n ):
		primes = []
		if n == 0 or n < 0:
			return primes
		elif n == 1:
			primes.append( 2 )
			return primes
		elif n == 2:
			primes.append( 2 )
			primes.append( 3 )
			return primes
		
		count = 0
		for idx in range( 2, ( 2 << 16 ) ):
			if self.isPrime( idx ):
				primes.append( idx )
				count += 1
			if count == n + 1:
				break
		
		return primes
			

def prime_home( request ):
	hypers = [ 
		HyperLinkContent( "./primecalc", "Prime by position", "Calculate prime number by specifying position..." ), 
		HyperLinkContent( "./load_primes", "Load prime numbers", "Load prime numbers by specifying position..." ),
		HyperLinkContent( "https://en.wikipedia.org/wiki/Prime_number", "Learn more", "Learn more about prime numbers on wikipedia..." )
	 ]
	dct = { "contents": hypers }
	return render( request, "prime_home.html", dct )
	
#prime calc page
def prime_calc( request ):
	prime = PrimeNumber()
	param = request.GET.get( 'primepos' )
	pos = int( 0 if param is None else param )
	val = prime.getPrimeAt( pos )
	dct = { "pos":pos, "val":val }
	return render( request, "primecalc.html", dct )

def load_primes( request ):
	prime = PrimeNumber()
	param_count = request.GET.get( 'count' )
	count = int( 0 if param_count is None else param_count )
	param_req_left = request.GET.get( 'left_req' )
	req_left = int( 0 if param_req_left is None else param_req_left )
	
	loadedAll = True
	left = 0
	to_load = count - 1
	if count > 10:
		left = count - 10
		loadedAll = False
		
		if req_left > 0:
			to_load = 10 + req_left
			req_left = 0
		else:
			to_load = 10
	else:
		to_load = count - 1
		
	primes = prime.getPrimes( to_load )
	
	return render( request, "load_primes.html", { "primes":primes, 							"loadedAll":loadedAll, "left":left } )
	
	
