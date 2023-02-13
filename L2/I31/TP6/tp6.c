#include <stdio.h>
#include <stdlib.h>
//gcc nom.c -o nom



typedef struct disque disque;
typedef struct tour tour;

struct disque{
  unsigned int size;
  disque* next;
};

struct tour{
  unsigned char id;
  unsigned int count;
  disque* first;
};

tour* newTour(unsigned char id){
  tour*t = (tour*)malloc(sizeof(tour));
  t -> id = id;
  t -> count = 0;
  t -> first = NULL;
  return t;
};

disque* newDisque(unsigned int s){
  disque*d = (disque*)malloc(sizeof(disque));
  d -> size = s;
  d -> next = NULL;
  return d;
};

void print(tour* t){
  printf("[");
  if ((t != NULL) && (t -> count != 0)){
    disque* current = t -> first;
    printf("%d", current -> size);
    current = current -> next;
    while (current != NULL){
      printf(", %d", current -> size);
      current = current -> next;
    }
  }
  printf("]\n");
}


int put(tour* t, disque* d){
  if ((t == NULL) || (d == NULL)){
    return 0;
  }

  if(t -> count == 0 ){
    t -> first = d;
    d -> next = NULL;
    t -> count++;
    return 1;
  }
  disque *d1 = t -> first;
  if(d1 -> size > d -> size){
    d -> next = d1;
    t -> first = d;
    t -> count++;
    return 1;
  }
  return 0;
}

disque* take(tour* t){
  if (t == NULL){
    return NULL;
  }
  disque* d = t -> first;
  if (d != NULL){
    t -> first = d -> next;
    t -> count -= 1;
  }
  return d;
}

int move(tour* origin, tour* destination){
  if((origin == NULL)||(destination == NULL)){
    return 0;
  }
  if(origin -> first == NULL){
    return 0;
  }
  disque* d = take(origin);
  if(d != NULL){
    int res=  put(destination, d);
    if(res==0) put(origin, d);
  }
  return 1;
}

void destroy(tour* t){
  if (t == NULL){
    return;
  }
  disque* current = t -> first;
  disque* next = NULL;
  while (current != NULL){
    next = current -> next;
    free(current);
    current = next;
  }
  free(t);
}



int main(){
  unsigned int ndisq, tourd, tourf;
  int c;
  tour* depart, *milieu, *fin;
  depart = newTour(1);
  milieu = newTour(2);
  fin = newTour(3);

  printf("Combien de disques voulez-vous jouer ?\n");
  scanf("%d", &ndisq);
  for (int i=ndisq; i>0;i--){
    put(depart(newDisque(i)));
  }
  printf("Vos disques sont dans la tour 1\n");
  tourd = 1;
  printf("Déplacer : 1 pour début, 2 pour millieu, 3 pour fin");
  scanf("%d", &tourf);
  if (move(tourd, tourf) == 0){
    return(printf("Déplacement impossible\n"));
  }
  else {
    c = move(tourd, tourf);

  }
  print(depart);
  print(milieu);
  print(fin);
  if (fin -> count == ndisq){
    printf("Gagné en X tours");
  }
/*
  print(depart);
  print(milieu);
  print(fin);
  move(depart,milieu);
  move(depart,fin);
  print(depart);
  print(milieu);
  print(fin);
  move(depart,milieu);
  print(depart);
  print(milieu);
  print(fin);*/
return 0;
}
