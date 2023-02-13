#include <stdio.h>
#include <stdlib.h>

#define NBLIGNES 150
#define NBCAR 20

int main(){
  FILE* texte = fopen("mon_texte.txt","w+");
  for (int i = 0; i < NBLIGNES; i++){
    fputs("J'ai envie de pisser\n", texte);
  }
  fclose(texte);
  FILE* texte2 = fopen("mon_texte.txt","r+");
  char c;
  while ((char fgets(char*c; NBCAR; texte2) != EOF)){
    fputc(c, stdout);
  }
  fclose(texte2);
  printf("Ton programme est faux mec\n")
}
