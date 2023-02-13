#include <stdio.h>
#include <stdlib.h>

void affiche_plateau(char plateau[3][3]){
  printf("[ %c %c %c ]\n", plateau[0][0], plateau[0][1], plateau[0][2]);
  printf("[ %c %c %c ]\n", plateau[1][0], plateau[1][1], plateau[1][2]);
  printf("[ %c %c %c ]\n", plateau[2][0], plateau[2][1], plateau[2][2]);
}

char case_valide(int ligne, int colonne, char plateau[][3]){
  if(ligne>=0 && ligne<3){
    if(colonne>=0 && colonne<3){
      if(plateau[ligne][colonne]==' '){
        return 1;
      }
    }
  }
  return 0;
}

char case_libre(char plateau[][3]){
  for(int i = 0; i<3; i++){
    for(int j = 0; j<3; j++){
      if(case_valide(i, j, plateau)==1){
        return 1;
      }
    }
  }
  return 0;
}

char aligne(char plateau[][3]){
 //vertical
  if(plateau[0][0]==plateau[0][1] && plateau[0][1]==plateau[0][2]){
    return 1;
  }
  else if(plateau[1][0]==plateau[1][1] && plateau[1][1]==plateau[1][2]){
    return 1;
  }
  else if(plateau[2][0]==plateau[2][1] && plateau[2][1]==plateau[2][2]){
    return 1;
  }
//horizontal
  else if(plateau[0][0]==plateau[1][0] && plateau[1][0]==plateau[2][0]){
    return 1;
  }
  else if(plateau[0][1]==plateau[1][1] && plateau[1][1]==plateau[2][1]){
    return 1;
  }
  else if(plateau[0][2]==plateau[1][2] && plateau[1][2]==plateau[2][2]){
    return 1;
  }
//diagonal
  else if(plateau[0][0]==plateau[1][1] && plateau[1][1]==plateau[2][2]){
    return 1;
  }
  else if(plateau[0][3]==plateau[1][1] && plateau[1][1]==plateau[2][0]){
    return 1;
  }
  return 0;
}

int main(int argc, char* argv[]){
  char plateau[3][3] = {{'X',' ','0'},{' ','X','O'},{' ','O','X'}};
  affiche_plateau(plateau);
  printf("%d\n", case_valide(0, 0, plateau));
  printf("%d\n", case_libre(plateau));
  printf("%d\n", aligne(plateau));
}
