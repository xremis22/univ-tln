#include <stdio.h>

void main(){
  int a, n, cpt;
  printf("saisir un nb\n");
  scanf("%d", &n);
  while (0 <= a <= 10){
    cpt += 1;
    a = n%10;
  }
  printf("%d", cpt);
}
