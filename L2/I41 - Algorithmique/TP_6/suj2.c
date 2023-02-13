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

uint IdxMin(int *T, uint a, uint b){
  int k, min = a;
  for(k = a + 1; k < b; k++){
    if(T[min] > T[k]){
      min = k;
    }
  }
  return min;
}

ullong TriSelection(int *T, uint n){
  int i = 1, imin, n = len(L);
  while(i < n){
    imin = IdxMin(L, i, n);
    echanger(L, i, imin);
    i += 1;
  }
  return L; 
}
