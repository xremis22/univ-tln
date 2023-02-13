#include <stdio.h>

int puissance(int x, int n){
  int c = x;
  for(int i = 1; i < n; i++){
    x *= c;
  }
  return x;
}
