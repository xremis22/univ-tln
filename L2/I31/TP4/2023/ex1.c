#include <stdio.h>
#include <stdlib.h>

void affiche(int t[], unsigned int n){
  if(n==0){
    printf("[ ]\n");
    return;
  }
  printf("[ %d,", t[0]);
  for(int i = 1; i<n-1; i++){
    printf(" %d,", t[i]);
  }
  printf(" %d ]\n", t[n-1]);
  return;
}

/*
int main(int argc, char* argv[]){
  unsigned int n;
  scanf("%d", &n);
  int *t = (int*)malloc(sizeof(n));
  for(int i = 0; i<n; i++){
    scanf("%d", &t[i]);
  }
  affiche(t, n);
}
*/
int main(int argc, char* argv[]){
  int t[4];
  for(int i = 0; i<=4; i++){
    printf("Entrez les valeurs du tableau une par une\n");
    scanf("%d", &t[i]);
  }
  affiche(t, 5);
}
