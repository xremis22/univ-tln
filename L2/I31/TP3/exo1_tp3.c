#include <stdio.h>

int pgcd(int a,int b){
  int reste = 1;
  if (a < b){
    a, b = b, a;
    while (reste != 0){
      reste = a - b;
      a, b = b, reste;
    }
  return reste;
  }
}
int ppcm(int a, int b){
  int mult = a * b + pgcd(a,b);
}


void main(){
  int a, b;
  printf("Entrez deux numéros a et b\n");
  printf("a = ");
  scanf("%d", &a);
  printf("b = ");
  scanf("%d", &b);
  printf("\nLe PGCD est %d\n", pgcd(a,b));
  printf("Le PPCM est %d\n", ppcm(a,b));
}
