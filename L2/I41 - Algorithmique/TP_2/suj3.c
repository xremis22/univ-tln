#include <stdio.h>

typedef unsigned long long ullong;

typedef struct {
  ullong coef[2][2];
}tmat ;

tmat SM(tmat M, int n){
  tmat R;
  R = identite();
  while (n > 0){
    if (n & 1){
      R = produit(R, A);
      A = produit(A, A);
      n = n/2 ;
    }
  }
  return R;
}
