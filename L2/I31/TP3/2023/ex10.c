#include <stdio.h>

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

int main(int argc, char* argv[]){
  int a, b;
  printf("Donnez la valeur de a : \n");
  scanf("%d", &a);
  printf("Donnez la valeur de b : \n");
  scanf("%d", &b);

  printf("%d\n", croissant(a, b));
}
