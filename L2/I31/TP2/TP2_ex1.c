#include <stdio.h>
int main(void)
{
   int a, b, c, o, k = 1;
   while (k == 1)
   {
       printf("Saisisez votre première variable\n");
       scanf(" %d", &a);
       printf("Saisisez votre deuxième variable\n");
       scanf(" %d", &b);
       printf("Saisisez votre opérateur\n");
       printf("1: +, 2: -, 3: x, 4: /, 5: modulo\n");
       scanf(" %d", &o);

       switch (o)
       {
       case 1:
           c = a + b;
           printf("a + b = %d\n", c);

           break;
       case 2:
           c = a - b;
           printf("a - b = %d\n", c);

           break;
       case 3:
           c = a * b;
           printf("a x b = %d\n", c);

           break;
       case 4:
           c = a / b;
           printf("a / b = %d\n", c);

           break;
       case 5:
           c = a % b;
           printf("a modulo b = %d\n", c);

           break;
       default:
           printf("Veuillez mettre un numéro correspondant à un opérateur\n");
           break;
       }
       printf("Voulez vous continuer ? 1 = oui / 0 = non\n");
       scanf("%d", &k);

   }
}
