#include <stdio.h>
#include <stdlib.h>





int main(void) {
  char p;
  FILE* var;
  FILE* fichier = NULL;
  var = fopen("entree.txt", "r");
  fichier = fopen("mes_caracteres.txt","w");
  while (!feof(var)){
    p = fgetc(var);
    fputc(p, fichier);
  }
  fclose(var);
}
