#include <stdio.h>

int main() {
 char c = 'A';
 int i = 66;
 float f = 67.6;

 printf("char avec %%c : %c\n", c);
 printf("char avec %%d : %d\n", c);
 printf("char avec %%f : %f\n", c);
 printf("char avec %%lf: %lf\n", c);

 printf("\n");
 printf("int avec %%c : %c\n", i);
 printf("int avec %%d : %d\n", i);
 printf("int avec %%f : %f\n", i);
 printf("int avec %%lf: %lf\n", i);
 printf("\n");
 printf("float avec %%c : %c\n", f);
 printf("float avec %%d : %d\n", f);
 printf("float avec %%f : %f\n", f);
 printf("float avec %%lf: %lf\n", f);
 return 0;
}
