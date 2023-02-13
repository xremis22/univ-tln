#include <stdio.h>


int prd(int x, int y){
  int z ;
  z = x * y;
  return z;
}

void proc(int t){
  char aux[100000]; /*variable inutilisée*/
  printf("t = %d\n", t);
  if (t<100){
    proc(t+1);
    t = 260000;
  }
}

int main(int argc, char* argv[]){
  int x, y, t;
  x = 13;
  y = 17;
  t = prd(x, y);
  printf("t = %d\n", t);
  return 0;
}
