#include <stdio.h>

float main(){
  float a,b,c;
  float moy;
  printf("saisir 3 nb\n");
  scanf("%f %f %f", &a, &b, &c);
  moy = (a + b + c)/2;
  printf("%f\n", moy);
}
