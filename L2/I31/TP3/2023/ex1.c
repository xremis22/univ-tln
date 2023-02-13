#include <stdio.h>

int pgcd(int a, int b){
  int c;
  while(b!=0){
    c = a;
    a = b;
    b = c%b;
  }
  return a;
}

int ppcm(int a, int b){
  return((a*b)/pgcd(a, b));
}

int factorielle(int n){
  int f = 1, i = 1;
  while(i<=n){
    f *= i;
    i += 1;
  }
  return f;
}

int puissance(int x, int n){
  int c = x;
  for(int i = 1; i < n; i++){
    x *= c;
  }
  return x;
}

unsigned int arrangement(unsigned int n, unsigned int k){
  unsigned int a = factorielle(n)/factorielle(n-k);
  return a;
}

unsigned int combinaison(unsigned int n, unsigned int k){
  unsigned int m = factorielle(n)/(factorielle(k)*factorielle(n-k));
  return m;
}

unsigned int polynewton(unsigned int x, unsigned int y, int n){
  unsigned int calc = 0;
  printf("%d^%d + ", combinaison(n, 0), calc);
  for(int i = 0; i <= n; i++){
    calc += combinaison(n, i)*puissance(x, n - i)*puissance(y, i);
    if(i==n){
      printf("%d^%d", combinaison(n, i), calc);
    }
    else {
        printf("%d^%d + ", combinaison(n, i), calc);
    }
  }

  return calc;
}

unsigned int newton(unsigned int x, unsigned int y, int n){
  unsigned int calc = 0;
  for(int i = 0; i <= n; i++){
    calc += combinaison(n, i)*puissance(x, n-i)*puissance(y, i);
  }
  return calc;
}

int inverse(int x){
  int r = 1/x;
  if(x==0){
    return 0;
  }
  else{
    return r;
  }
}

int croissant(int a, int b){
  int max;
  if(a>b){
    max = a;
  }
  else if(a<b){
    max = b;
  }

  else{
    max = 0;
  }
  if(max==0){
    return(printf("Les deux éléments sont égaux\n"));
  }
  else{
    return(max);
  }
}

int main(int argc, char* arv[]){
  int a, b, x, n, k, y;
  printf("Entrez la valeur de a : \n");
  scanf("%d", &a);
  printf("Entrez la valeur de b : \n");
  scanf("%d", &b);
  printf("Entrez la valeur de x : \n");
  scanf("%d", &x);
  printf("Entrez la valeur de y : \n");
  scanf("%d", &y);
  printf("Entrez la valeur de n : \n");
  scanf("%d", &n);
  printf("Entrez la valeur de k : \n");
  scanf("%d", &k);

  printf("PGCD(%d, %d) = %d\n", a, b, pgcd(a,b));
  printf("PPCM(%d, %d) = %d\n", a, b, ppcm(a, b));
  printf("fact(%d) = %d\n", n, factorielle(n));
  printf("%d^%d = %d\n", x, n, puissance(x, n));
  printf("Arrangement de k = %d\n", arrangement(n, k));
  printf("Combinaison de %d éléments d'un ensemble E de %d éléments = %d\n", k, n, combinaison(n, k));
//  printf("newton(%d, %d, %d) = %d\n", x, y, n, newton(x, y, n));
  printf("L'inverse de %d est = %d\n", x, inverse(x));
}
