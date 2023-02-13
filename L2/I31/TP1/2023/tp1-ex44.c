#include <stdio.h>


int main(){
  int x, y, z;
  scanf("%d %d %d", &x, &y, &z);
  printf("Les valeurs sont x = %d, y = %d, z = %d\n \n \n", x, y, z);
  printf("++x || (++y > z && (y* ++z)) = %d\n", ((++x || (++y > z && (y* ++z)))));

  return 0;
}
