#include <stdio.h>

typedef enum{
  FAUX = 0,
  VRAI = 1
} tbool;

tbool CommencePar(char * mot, char *deb){
  for(int i = 0; i < 10; i++){
    if (mot[i] != deb[i]){
      return FAUX;
    }
  }
  return VRAI;
}

tbool BienParenthesee(char * expr){
  int k = 0, l = 0;
  /*Il faut surtout pas mettre d'espace dans l'expression ! */
  for(int i = 0; expr[i] != '\0'; i++){ /*tant que expr[i] != fin de caractère*/
    if (expr[i] == '('){
      k += 1;
    }
    if (expr[i] == ')'){
      l += 1;
    }
    if (l > k){
      return FAUX;
    }
  }
  if (k != l){
    return FAUX;
  }//
  return VRAI;
}

int main(void){
  char mot[10], deb[10], expr[100];
  printf("Entrez la première chaîne : \n");
  scanf("%s", mot);

  printf("Entrez la deuxième chaîne : \n");
  scanf("%s", deb);

  printf("Chaîne 1 : %s\n Chaîne 2 : %s\n", mot, deb);

  printf("Entrez votre expression : \n");
  scanf("%s", expr);

  BienParenthesee(expr);

  if(BienParenthesee(expr) == VRAI){
    printf("L'expression était bien parenthésée\n");
  }
  else {
    printf("L'expression contenait des erreures\n");
  }
}
