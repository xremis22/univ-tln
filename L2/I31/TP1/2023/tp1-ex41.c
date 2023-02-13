#include <stdio.h>

int date, a, m, j;

int main(){
  scanf("%d", &date);
  j = date%100;
  m = (date%10000 - date%100)/100;
  a = (date%100000000 - m*100 - j)/10000;
  printf("La date saisie au clavier est %d/%d/%d\n", j, m, a);
  return 0;
}
