#include <stdio.h>

int factorielle(int n){
  int f = 1, i = 1;
  while(i<=n){
    f *= i;
    i += 1;
  }
  return f;
}
