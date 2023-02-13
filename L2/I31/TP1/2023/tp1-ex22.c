#include <stdio.h>
char c = 65; //valeur ascii de a
int i = 2;
float f = 3.0;
double d = 4.0;

int main(){
  printf("c = %d, i = %d, f = %f, d = %f\n", c, i, f, d);
  c += 4;
  i += 4;
  f += 4.0;
  d += 4.0;
  printf("c = %d, i = %d, f = %f, d = %f\n", c, i, f, d);
}
