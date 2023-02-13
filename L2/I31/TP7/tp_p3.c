#include <stdio.h>
#include <stdlib.h>
#include "date.h"
#include "personne.h"


typedef struct  membre_famille membre_famille;


struct membre_famille{
  personne* individu;
  membre_famille* pere;
  membre_famille* mere;
};

membre_famille* nouveau_membre(personne* i, personne* p, personne* m){
    membre_famille* m=(membre_famille*)malloc(sizeof(membre_famille));

}
