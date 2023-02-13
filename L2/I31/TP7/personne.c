#include <stdio.h>
#include "date.h"
#include "personne.h"


personne* alloue_p(){
  personne* p = (personne*)malloc(sizeof(personne));
  p -> nom = (char*)malloc(sizeof(char)*50);
  p -> prenom = (char*)malloc(sizeof(char)*50);
}
personne* saisie_personne(){
  personne* p = alloue_p();
  printf("Saisisez le nom, prénom, date de naissance et décès\n");
  scanf("%s %s", p -> nom, p -> prenom);
  p -> date_naissance = saisie_date();
  p -> date_deces = saisie_date();
  return p;
}

void affiche_personne(personne* p){
  printf("%s %s ",p -> nom, p -> prenom);
  affiche_date(p -> date_naissance);
  printf(" - ");
  affiche_date(p -> date_deces);
}

int meme_personne(personne* p1, personne* p2){
  if (p1 -> nom == p2 -> nom){
    if (p1 -> prenom == p2 -> prenom){
      if ((date_compare(p1 -> date_naissance, p2 -> date_naissance) == 0)
      && (date_compare(p1 -> date_deces, p2 -> date_deces) == 0)){
        return 1;
      }
    }
  }
  else {
    return 0;
  }
}
