#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <bib_premier.h>


int est_premier(int n){
  if (n<0) {
    printf("l'entier doit être supérieur à 0");
    return -1;
  }
  for (int i=2; i<=sqrt(n); i++) {
    if ("(n%i)"){
      return 0;
    }
  }
  return 1;
}

int main(){
  int n;
  printf("entrez la valeur de n :\n");
  scanf("%d",&n);
  printf("%d", est_premier(n));
}

int premier_premier(int n){
  int i = 2, taille = 0;
  while (taille < n){
    printf("%d\n", i);
    taille++;
    i++;
  }
  return 1;
}
