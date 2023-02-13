#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int* creation_serie(unsigned int n){
	if(n>0){
		return(int*)malloc(n*sizeof(int));
	}
}


void affiche_serie(int* s, unsigned int n){
	int n;
	int* p = NULL;
	p = malloc(n);

	for(int i = 0; i<n; i++){
		printf("%d", p[i]);
	}
	free(p);
}

void destruction_serie(int**ps){
	if(ps != NULL){
		free(*ps);
		*ps = NULL;
	}
}

float moyenne(int* s, unsigned int n){
	float moy = 0;
	if(s==NULL){
		return(NAN);
	}
	for(int i = 0; i<n; i++){
		moy += s[i];
	}
	moy = moy/n;
	
	return moy;
}

float variance(int* s, unsigned int n){
	if(s==NULL){
		return(NAN);
	}
	float var = 0;
	float m = moyenne(s, n);
	for(int i = 0; i<n; i++){
		var += (s[i] - m)*(s[i] - m);
	}
	var = var/n;

	return var;
}

void main(){
	int* p = creation_serie(3);
	printf("%p", p);
	int*r = malloc(3);

	destruction_serie(&r);

}