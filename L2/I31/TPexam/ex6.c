#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct date date;
struct date{
  unsigned int jour;
  unsigned int mois;
  unsigned int annee;
};

typedef struct element element;
struct element{
  date val;
  element* next;
};

typedef struct stack stack;
struct stack{
  unsigned int ndate;
  element* first;
}

stack* newStack(){
  stack* s = (sack*)malloc(sizeof(stack));
  s -> size = 0;
  s -> first = NULL;
  return s;
}

date* NewDate(date val){
  date* d = (date*)malloc(sizeof(date));
  d -> val = val;
  d -> next = NULL;
  return d;
}

int push(stack* p, date* d){
  if ((p == NULL) || (d == NULL )){
    return 0;
  }
  d -> next = p-> first;
  p -> first = d;
  p -> size += 1;

  return 1;
}

int pushd(stack* p, date d){
  if (p == NULL){
    return 0;
  }
  return push(p, newDate(d));
}

int main(){
  int a, p, d1;
  printf("1. Ajouter une date\n2. Depiler jusqu'à la date\n3. Quitter\nEntrer votre choix:\n");
  scanf("%d", &a);
  if (a == 1){
    d1 = NewDate(1);
    push(p, d1);
  }
  else if (a == 2){

  }
}
