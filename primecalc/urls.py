from django.urls import path

from . import views

urlpatterns = [
	path( '', views.prime_home, name='home' ),
	path( 'load_primes/', views.load_primes, name='loadprimes' ),
	path( 'primecalc/', views.prime_calc, name='posprime' )
]
