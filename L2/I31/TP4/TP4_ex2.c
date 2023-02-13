#include <stdio.h>
#include <stdlib.h>

char p[30];

int main(void) {
  FILE* fichier = NULL;
  fichier = fopen("mes_caracteres.txt","w");
  if (fichier != NULL)
  {
    printf("Veuillez entrer une phrase\n");
    //scanf("%s", p);
    //fprintf(fichier, "%s", p);
    gets(p);
    fputs(p, fichier);

  }
}
