#include <stdio.h>
/*
int main(){
  char a;
  a = scanf("%s", a);
  printf("%s", a);
  printf("Hello World\n");
  return 0;
}*/

int main(int argc, char *argv[])
{
    for (int i = 1; i < argc; i++) {
	puts(argv[i]);
    }
    printf("Hello World\n");
    return 0;
}
