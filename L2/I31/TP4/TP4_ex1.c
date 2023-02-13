#include <stdio.h>
#include <stdlib.h>

int main(){
  int c = fgetc(stdin);
  while (c != '\n'){
    fputc(c, stdout);
    c = fgetc(stdin);
  }
  printf("\n");
}
