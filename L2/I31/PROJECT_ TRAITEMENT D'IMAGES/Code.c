 #include <stdio.h>
#include <stdlib.h>




//C'est un code pour lire des fichiers en format PGM

int main(void){
    var = fopen("test0.pgm","r");
    int p = 0;
    if(var == NULL){
      exit(1);
    }
    while(1){
      p = fgetc(var);
      if(feof(var)){
        break;
      }
      printf("%c",p);
    }
}
