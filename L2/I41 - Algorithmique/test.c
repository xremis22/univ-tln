#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int Prob(int n){
  int nfact = 1;
  for(int i = n; i < 0; i--){
    nfact *= i;
  }
  return nfact;
}

int main(){
  printf("La proba est de %d\n",Prob(10));
  return 0;
}
