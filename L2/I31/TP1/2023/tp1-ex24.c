#include <stdio.h>


float x = 1.0, y = 2.0, z = 3.0, u = 4.0, v = 5.0, w = 6.0;

int main(){
  printf("%f, %f, %f, %f\n", (x+2)/(y+4), x*(y + z*(3 - u)), (x*y)/(v+2), (u*x*x*x + v*x*x + w*x));
  return 0;
}
