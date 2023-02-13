#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define  max  8
void test()
{
     puts("\nOoops !"); 
     printf("test=%p\n", test );
     exit(2);
}
void strcopy( char *d, char*s )
{
while (*s) *d++ = *s++;
}

void doit(char *s)
{
    char t[max];
    strcopy( t, s );
}


int main(int argc, char *argv[])
{
    doit(argv[1]);
    putchar('\n');
    return 0;
}
