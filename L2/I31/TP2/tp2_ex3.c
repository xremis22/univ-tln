#include <stdio.h>

void main(){
  int n, cpt, nb;
  printf("Entrez un nombre : \n");
  scanf("%d",&n);
  nb = n;
  cpt = 0;
  do {
    nb = nb/10;
    cpt += 1;
  }
  while ((nb)!=0);
  printf("Le nombre de chiffres de %d est %d \n", n, cpt);
}
