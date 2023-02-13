#include <stdio.h>

int saisie_date(unsigned int j, unsigned int m, unsigned int a){
  if(j<32){
    if(m<13){
      if(a<2023){
        return 1;
      }
    }
  }
  else{
    return 0;
  }
}

int main(int argc, char* argv[]){
  int j, m, a;
  printf("Veuillez entrer votre date de naissance au BON format : \n");
  scanf("%d/%d/%d", &j, &m, &a);
  if(saisie_date(j, m, a)==1){
    printf("La date a été écrite au bon format\n");
  }
  else {
    printf("Tu es une grosse merde\n");
  }
}
