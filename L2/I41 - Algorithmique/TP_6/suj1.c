#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


typedef unsigned int uint;
typedef unsigned short ushort;

void echanger(uint *L, uint i, uint j){
  int bis;
  bis = L[i];
  L[i] = L[j];
  L[j] = bis;
}


uint *GenPerm(uint n){
  uint *tab = (void*)malloc(sizeof(tab));
  int a = 1;
  for(int i = 0; i < n; i++){
    tab[i] = a;
    a++;
  }
  for(int j = 0; j < n; j++){
    echanger(tab, j, rand()%n);
  }
  return tab;
}

int main(int argc, char * argv[]){
  srand(time(NULL));
  printf("%d\n", GenPerm(5));
}
