#include <stdio.h>
int main(void)
{
 char c1, c2;
 int i;
 float f;
 printf("Entrer un entier: ");
 scanf("%d", &i);
 printf("i = %d\n", i);

 printf("Entrer un reel: ");
 scanf("%f", &f);
 printf("f = %f\n", f);

 printf("Entrer un caractere: ");
 getchar(); //reinitialiser le buffer
 scanf("%c", &c1);
 printf("c1 = %c\n", c1);

 printf("Entrer un autre caractere: ");
 getchar(); //reinitialiser le buffer
 scanf("%c", &c2);
 printf("c2 = %c\n", c2);

 return 0;
}
