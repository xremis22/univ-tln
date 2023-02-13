#include <stdio.h>
#include <math.h>

int main(){
  float a, b, c, delta, x1, x2;
  printf("Entrez les valeurs de a, b, et c = \n");
  scanf("%f", &a);
  getchar();
  scanf("%f", &b);
  getchar();
  scanf("%f", &c);
  getchar();

  delta = b*b - 4*a*c;
  if(delta<0){
    return(printf("Le polynôme n'admet pas de solutions dans les réels\n"));
  }
  else if(delta == 0){
    x1 = (-b)/(2*a);
    return(printf("La solution de l'équation du second degré est %f\n\n\n", x1));
  }
  else {
    x1 = (-b-(sqrt(delta)))/(2*a);
    x2 = (-b+(sqrt(delta)))/(2*a);

    return(printf("L'équation admet deux solutions x1 = %f, et x2 = %f\n\n\n", x1, x2));
  }
}
