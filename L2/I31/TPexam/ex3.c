#include <stdio.h>

int main(){
  int i = 0, n;
  printf("saisir un nb\n");
  scanf("%d", &n);
  while(i<n){
    i += 1;
    printf("%d\n",i);
  }
}
