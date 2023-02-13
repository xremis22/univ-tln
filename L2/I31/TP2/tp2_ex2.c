#include <stdio.h>

void main(){
  int a, c, i;
  i = 1;
  c = 0;
  printf("Entrez un nombre : \n");
  scanf("%d",&a);
  while (c <= a) {
    c = i*i;
    i += 1;
  }
  printf("Le plus petit carré supérieur à %d est %d\n", a, c);
}
