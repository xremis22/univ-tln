#include <stdio.h>

int factorielle(int n){
  int f = 1, i = 1;
  while(i<=n){
    f *= i;
    i += 1;
  }
  return f;
}

unsigned int arrangement(unsigned int n, unsigned int k){
  unsigned int a = factorielle(n)/factorielle(n-k);
  return a;
}
