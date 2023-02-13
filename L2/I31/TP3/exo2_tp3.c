#include <stdio.h>
#include <stdlib.h>

int factorielle(int n)
{
	if (n < 0)
	{
		printf("n ne peut pas être négatif!\n");
		exit(EXIT_FAILURE);
	}
	int j = 1;
	for (int i = n; i > 0; i--)
		j *= i;
	return j;
}

void main(){
  int n;
  printf("Entrez n\n");
  printf("n = ");
  scanf("%d", &n);
  printf("%d! = %d\n", n, factorielle(n));
}
