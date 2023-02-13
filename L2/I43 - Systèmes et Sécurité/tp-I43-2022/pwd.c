#include <stdio.h>
#include <crypt.h>
#define _XOPEN_SOURCE       /* See feature_test_macros(7) */
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define max 32
#define joker  74
#define admin  666

typedef struct {
	char pseudo[max];
	char nop;
	int  flag;
} user_t;

void hashpass ( user_t * w )
{
  char  *r;
  printf("%s...\n", w->pseudo);
  r = crypt( w->pseudo , "tegNlzW5VjNcM" );
  if ( 0 == strcmp( r , "tegNlzW5VjNcM" ))
      w->flag = admin;
  
  r = crypt( w->pseudo , "teH1QmymLm6ws" );
  if ( 0 == strcmp( r , "teH1QmymLm6ws" ))
      w->flag = joker;
}



int main( void )
{
user_t w;
int cpt = 0;
while ( w.flag != joker && w.flag != admin && cpt < 3) {
  printf("\n%d hash ? ", cpt);
  scanf("%s", & w.pseudo );
  hashpass( &w );
  cpt++;
}

if ( cpt == 3 ) 
	exit( 1 );
printf("\nBonjour  nop=%c flag=%d!\n", w.nop, w.flag);
switch( w.flag ) {
	case joker : puts("joker"); break;
	case admin : puts("admin"); break;
	default   : puts("autre"); break;
}
return 0;
}
