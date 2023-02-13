#include <stdio.h>

int main(){
  int x, y, z, w;
  printf("Donnez les coordonnées de v1 : \n");
  scanf("%d", &x);
  scanf("%d", &y);
  printf("Donnez les coordonnées de v2 : \n");
  scanf("%d", &z);
  scanf("%d", &w);

  printf("Produit scalaire de v1 et v2 : %d\n", x*z + y*w);
  return 0;
}
