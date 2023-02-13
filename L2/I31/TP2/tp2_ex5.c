#include <stdio.h>
/*
int moyenne(int *valeurs, int size);
int variance(int *valeurs, int size);

int main(){
  unsigned int n;
  printf("Entrez un nombre \n");
  scanf("%d",&n);
  int valeurs[n];
  int valeurs_size = 0;

  for(int i = 0; i<n; i++){
    scanf("%d",&valeurs[i]);
  }

  int moy = moyenne(valeurs, valeurs_size);
  int var = variance(valeurs, valeurs_size);

  printf("Moyenne %d\n", moy);
  printf("Variance %d\n", var);
}

int moyenne(int *valeurs, int size){
  int moyenne = 0;
  for (int i = 0; i < size; i++){
    moyenne += valeurs[i];
  }
  return moyenne/size;
}

int variance(int *valeurs, int size){
  int variance =0;
  int moy = moyenne(valeurs, size);
  for (int i = 0; i < size; i++){
    int term = (valeurs[i] - moy);
    variance += term * term;
  }
  return variance/size;
}
*/

int main(){
  int i = 0;
  float n, r = 0;
  do {
    printf("Entrez un nombre (<0 pour terminer)\n");
    scanf("%f", &n);
    if(n<0){
      break;
    }
    r += n;
    i ++;
  }
  while (n>0);
  return(printf("La moyenne des nombres est %f\n\n\n", r/i));
}
