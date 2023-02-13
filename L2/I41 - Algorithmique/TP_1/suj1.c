#include <stdio.h>
/*gcc -Wall -g TP3.c*/

typedef unsigned long long ulong;
typedef unsigned char uchar;

int main(){
    uchar B[] = { 0, 0, 0, 0, 0 };

    uchar Increment(uchar * A, uchar n , uchar b){ /*Tableau A de n entiers en base b*/
      int k = 0;
      for (int i = 0; i <= n, i++;){
        if (A[i] == (b - 1)){
          A[i] = 0;
        }
        else {
          A[i] += 1;
          break ;
        }
        k ++;
      }
      return k;
      printf("%d", k);
    }


    printf("%d\n", Increment(4 , B, 10));
}

ullong test(uchar n, uchar b){
  ullong r = 1;
  if (b > 255){
    return -1;
  }
  while ((n > 0 ) && (n<=255)){
    r *= b;
    n -= 1;
  }
  return r;
}
