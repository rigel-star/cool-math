/* '' *********** TEST CODE YOU CAN IGNORE THIS ********* ''' */
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

const char ops[] = { '-', '+', '/', '*', '^' };

char*
analyze( char [], int );

int
isoperator( char );

int main( void ) {

  char* expr = "-22+22";
  char* res = analyze( expr, 5 );
  printf( "\n\nInput:: %s\n", expr );
  printf( "Result:: %s\n\n", res );
  return 0;
}

int
isoperator( char c ) {
  int is = 0;
  for ( int i = 0; i < 5; i++ ) {
    if ( c == ops[i] ) {
      is = 1;
      break;
    }
  }
  return is;
}

char*
analyze( char expr[], int size ) {
  //size_t size = sizeof( expr );
  char* res = malloc( sizeof( char ) * 100 );
  char* tmp = malloc( sizeof( char ) * 1 );
  for ( int i = 0; i < size; i++ ) {
    if ( expr[i] == '-' ) {
      if ( i == 0 ) {
        strcat( res, "-" );
        for ( int j = i + 1; j < size; j++, i++ ) {
          if ( isdigit( expr[i] ) ) {
            *tmp = expr[j];
            strcat( res, tmp );
          }
          else {
            *tmp = expr[j];
            strcat( res, " " );
            strcat( res, tmp );
            strcat( res, " " );
          }
        }
      }
      else {
        strcat( res, "-" );
        strcat( res, " " );
      }
    }
    else if ( isdigit( expr[i] ) ) {
      *tmp = expr[i];
      strcat( res, tmp );
      for ( int j = i + 1; j < size; j++, i++ ) {
        if ( isdigit( expr[j] ) ) {
          *tmp = expr[j];
          strcat( res, tmp );
        }
        else {
          *tmp = expr[j];
          strcat( res, tmp );
          strcat( res, " " );
          break;
        }
      }
    }
    else if ( expr[i] == ' ' ) {
      strcat( res, " " );
    }
    else if ( isoperator( expr[i] ) ) {
      *tmp = expr[i];
      strcat( res, tmp );
      strcat( res, " " );
    }
  }
  free( tmp );
  return res;
}
