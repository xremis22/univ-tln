#include <stdio.h>

typedef unsigned long long ullong;

typedef struct {
  ullong coef[2][2];
}tmat ;

tmat produit(tmat A, tmat B){
  tmat R;
  for(int i = 0; i < sizeof(A); i++){
    for (int j = 0; j < sizeof(A); i++){
      R[i][j] = 0;
      for(int k = 0; k < sizeof(A); k++){
        R[i][j] += A[i][k]*B[k][j];
      }
    }
  }
  return R;
}
