#include <stdio.h>
#include <stdlib.h>

int main(void){
  int tab[10], nbr, i;

  printf("Nombre à convertir : ");
  scanf("%d", &nbr);

  for(i=0; nbr > 0; i++){
    tab[i] = nbr%2;
    nbr = nbr/2;
  }
  printf("\nLe nombre bianire est : \n");

  for(i=i-1; i >=0 ; i--){
    printf("\n%d   ", tab[i]);
  }
}
