#include <stdio.h>

int a, b, expr;

int main(){
  expr = a&!b || !a&b;
  printf("Donnez les valeurs de a et de b\n");
  scanf("%d", &a);
  scanf("%d", &b);
  printf("expr = %d\n", expr);
}
