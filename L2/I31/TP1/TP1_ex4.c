#include <stdio.h>

int main(void){
  int x, y ,m;
  printf("Saisisez votre première variable\n");
  scanf("%d",&x);
  printf("Saisisez votre deuxième variable\n");
  scanf("%d",&y);
  if (x > y){
    m = x ;
  }
  else if (x == y){
    printf("Les deux nombres sont égaux\n");
    return 0;
  }
  else {
    m = y ;
  }
  printf("Le max est : %d\n",m);
}
