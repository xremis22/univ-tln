#include <stdio.h>
#include <stdlib.h>


int main(void){
  int nbr = 0, i;
  char p[4];                                                      /*table p a 4 cases pour extraire les chiffres en binaire*/
  FILE* var;
  FILE* fichier;
  fichier = fopen("test.txt","w");                                /*pointeur fichier referencie le fichier a editer*/
  var = fopen("test0.pgm","r");                                   /*pointeur var referencie le fichier a lire*/
  while(!feof(var)){                                              /*condition d'arret : end of file*/
    if(isdigit(p)){                                               /*verifie que l'element qu'on etudie est bien un chiffre*/
      fgets(p, 3, var);                                           /*copie 3 caracteres et les renvoie dans le pointeur*/
      printf("%s", p);                                            /*ligne de verification*/

      for(i = 0; i < nbr; i++){                                   /*transforme les nombres decimales en binaire*/
        p[i] = nbr%2;
        nbr = nbr/2;
      }
      printf("\nBin = ");
      for(i -= 1; i >= 0; i--){                                   /*Donne le résultat de la transformation en binaire*/
        printf("%c", p[i]);
      }
      fputs(p, fichier);
    }
  }
  fclose(fichier);
  fclose(var);
}
