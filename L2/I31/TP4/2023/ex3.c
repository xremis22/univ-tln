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


void extremum(int t[], unsigned int n, unsigned int* min, unsigned int* max){
  *min = t[0];
  *max = t[n-1];
  for(int i = 0; i<n; i++){
    if(t[i]<*min){
      *min = t[i];
    }
    if(t[i]>*max){
      *max = t[i];
    }
  }
  printf("min = %d\n", *min);
  printf("max = %d\n", *max);
}

int main(int argc, char* argv[]){
  int t[4];
  for(int i = 0; i<=4; i++){
    printf("Entrez les valeurs du tableau une par une\n");
    scanf("%d", &t[i]);
  }
  unsigned int min, max;
  affiche(t, 4);
  extremum(t, 4, &min, &max);
}
