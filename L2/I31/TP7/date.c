#include <stdio.h>
#include "date.h"


date saisie_date(){
  date d;
  printf("Saisisez la date en respectant JJ/MM/AAAA\n");
  scanf("%02u/%02u/%04u", &d.jour, &d.mois, &d.annee);
  return d;
}

void affiche_date(date d){
  printf("%02u/%02u/%04u\n", d.jour, d.mois, d.annee);
}

int date_compare(date d1, date d2){
  if (d1.annee < d2.annee){
    return -1;
  }
  if (d1.annee == d2.annee){
    if (d1.mois < d2.mois){
      return -1;
    }
    if (d1.mois == d2.mois){
      if (d1.jour < d2.jour){
        return -1;
      }
      if (d1.jour == d2.jour){
        return 0;
      }
      else {
        return 1;
      }
    }
    else {
      return 1;
    }
  }
  else {
    return 1;
  }
}
