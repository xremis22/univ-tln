#include <stdio.h>

int main(){
  int a;
  printf("saisir un nb\n");
  scanf("%d", &a);
  if (a > 12){
    printf("Le chiffre saisi doit être entre 1 et 12\n");
  }
  if(a==1){
    printf("Janvier\n");
  }
  if(a==2){
    printf("Février\n");
  }
  if(a==3){
    printf("Mars\n");
  }
  if(a==4){
    printf("Avril\n");
  }
  if(a==5){
    printf("Mai\n");
  }
  if(a==6){
    printf("Juin\n");
  }
  if(a==7){
    printf("Juillet\n");
  }
  if(a==8){
    printf("Août\n");
  }
  if(a==9){
    printf("Septembre\n");
  }
  if(a==10){
    printf("Octobre\n");
  }
  if(a==11){
    printf("Novembre\n");
  }
  if(a==12){
    printf("Décembre\n");
  }
}
