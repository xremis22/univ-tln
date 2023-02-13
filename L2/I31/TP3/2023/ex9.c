#include <stdio.h>

int inverse(int x){
  int r = 1/x;
  if(x==0){
    return 0;
  }
  else{
    return r;
  }
}
