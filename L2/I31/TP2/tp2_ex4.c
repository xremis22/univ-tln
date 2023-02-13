#include <stdio.h>

void main(){
  int n, s_carre = 0;
  printf("Entrez un nombre : \n");
  scanf("%d",&n);
  if (n<=0){
    printf("Poto t'as pas lu l'énoncé ou kwa ? \n");
  }
  else {
    for(int i=1; i <= n; i++){
      s_carre += i*i;
    }
  }

  if (n>0){
    printf("La somme des carrés jusqu'à %d est égal à %d\n",n, s_carre);
  }
}
