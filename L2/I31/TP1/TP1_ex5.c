#include <stdio.h>

int main(){
  int a, m, j, d;
  printf("Saisisez la date codéinée\n");
  scanf("%d",&d);
  a = d/10000;
  m = (d%10000)/100;
  j = (d%10000)%100;
  printf("jour : %d\nmois : %d\nannée :%d\n", j, m, a);
}
