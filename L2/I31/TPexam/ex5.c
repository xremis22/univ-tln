#include <stdio.h>
#include <math.h>

int main(){
  float rac1, rac2, pt_r, pt_c;
  int delta, a, b, c;
  printf("saisir la valeur de a, b, c\n");
  scanf("%d %d %d", &a, &b, &c);
  delta = b*b - (4*a*c);
  if (delta > 0){
    rac1 = (((-b)+sqrt(delta))/(2*a));
    rac2 = (((-b)-sqrt(delta))/(2*a));
    printf("racine 1 = %f, racine 2 = %f\n",rac1, rac2);
  }
  else if (delta < 0){
    delta = -delta;
    pt_r = ((-b)/(2*a));
    pt_c = ((sqrt(delta))/(2*a));
    printf("racine 1 = %f + i%f, racine 2 = %f - i%f\n", pt_r, pt_c, pt_r, pt_c);
  }
  else {
    rac1 = ((-b)/(2*a));
    printf("racine = %f\n", rac1);
  }
}
