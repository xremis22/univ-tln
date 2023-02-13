#include <stdio.h>
#define PI 3.141592653589793

int main(){
  float r, aire, perimetre;
  printf("Donnez le rayon du cercle : \n");
  scanf("%f", &r);
  perimetre = 2*PI*r;
  aire = PI*r*r;
  printf("L'aire = %f, périmètre = %f\n", aire, perimetre);
}
