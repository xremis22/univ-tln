#include <stdio.h>

int pgcd(int a, int b){
  int c;
  while(b!=0){
    c = a;
    a = b;
    b = c%b;
  }
  return a;
}

int ppcm(int a, int b){
  return((a*b)/pgcd(a, b));
}
