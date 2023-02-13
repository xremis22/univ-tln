#include <stdio.h>


int main(int argc, char* argv[]){
  int n;
  printf("Donnez la valeur de n : \n");
  scanf("%d", &n);
  do{
    printf(" x^%d +", n--);
    if(n==0){
      printf(" 1\n\n\n");
      break;
    }
  }
  while(n>0);
  return 0;
}
