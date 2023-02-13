#include <stdio.h>
#include <stdlib.h>

int somme(int t[], unsigned int n){
  if(n==0){
    printf("Le tableau est vide\n");
    return 0;
  }
  int s = 0;
  for(int i = 0; i<n; i++){
    s += t[i];
  }
  return(printf("la somme des valeurs du tableau est égale à : %d\n", s));
}

int main(int argc, char* argv[]){
  int t[4];
  for(int i = 0; i<=4; i++){
    printf("Entrez les valeurs du tableau une par une\n");
    scanf("%d", &t[i]);
  }
  somme(t, 5);
}
