#include <stdio.h>

typedef struct personne personne;
struct personne{
  char* nom;
  char* prenom;
  date date_naissance;
  date date_deces;
};

personne* alloue_p();
personne* saisie_personne();
void affiche_personne(personne* p);
int meme_personne(personne* p1, personne* p2);
