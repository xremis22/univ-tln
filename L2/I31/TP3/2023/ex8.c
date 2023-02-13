#include <stdio.h>

int factorielle(int n){
  int f = 1, i = 1;
  while(i<=n){
    f *= i;
    i += 1;
  }
  return f;
}

unsigned int combinaison(unsigned int n, unsigned int k){
  unsigned int m = factorielle(n)/(factorielle(k)*factorielle(n-k));
  return m;
}

int puissance(int x, int n){
  int c = x;
  for(int i = 1; i < n; i++){
    x *= c;
  }
  return x;
}

unsigned int newton(unsigned int x, unsigned int y, int n){
  unsigned int calc = 0;
  for(int i = 0; i <= n; i++){
    calc += combinaison(n, i)*puissance(x, i)*puissance(y, n-i);
  }
  return calc;
}

int main(int argc, char* argv[]){
  int x, y, n;
  printf("Entrez la valeur de x : \n");
  scanf("%d", &x);
  printf("Entrez la valeur de y : \n");
  scanf("%d", &y);
  printf("Entrez la valeur de n : \n");
  scanf("%d", &n);

  //printf("écriture polynomiale de (%d + %d)^%d est : %d", x, y, n, newton(x, y, n));
  printf("%d\n", newton(x, y, n));
}
