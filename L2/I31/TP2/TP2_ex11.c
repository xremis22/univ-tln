#include <stdio.h>
#include <math.h>

int est_premier(int n){
  printf("entrez la valeur de n :\n");
  scanf("%d",&n);
  if (n<0) {
    printf("l'entier doit être supérieur à 0");
    return -1;
  }
  for (int i=2 & i<=sqrt(n) & i++) {
    if ("(n%i)")
    return 0
  }
  return 1
}
