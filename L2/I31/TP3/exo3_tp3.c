#include <stdio.h>
#include <stdlib.h>

int puissance(int x, int n){
  int resultat = 1;
  if (n < 0){
    printf("pas de puissances négatives\n");
    return 0;
  }
  else {
    for (int i = 0; i <= n; i++){
      resultat *= x;
    }
  }
  return resultat;
}


int main(){
  int x, n;
  printf("x = ");
  scanf("%d", &x);
  printf("n = ");
  scanf("%d", &n);
  printf("%d\n", puissance(x,n));
}
