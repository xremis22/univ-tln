#include <stdio.h>

typedef struct date date;
struct date{
  unsigned int jour;
  unsigned int mois;
  unsigned int annee;
};

date saisie_date();

void affiche_date(date d);

int date_compare(date d1, date d2);
