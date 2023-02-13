#include <stdio.h>
#include <stdlib.h>
#include <SDL2/SDL.h>

int main(void){
  unsigned int t = 0;
  unsigned int c = 0;
  unsigned int x = 0;
  unsigned int y = 0;

  unsigned int frame_width = 500;
  unsigned int frame_height = 500;

  unsigned int column_width = 0;
  unsigned int row_height   = 0;

  unsigned int rows = 10;
  unsigned int columns = 10;

  //unsigned int col = 0;

  SDL_Window* fenetre;
  SDL_Renderer* renderer;
  SDL_Rect cell = {x, y};

  printf("Nombre de lignes : ");
  scanf("%d", &rows);

  printf("Nombre de colonnes : ");
  scanf("%d", &columns);
/*
  printf("Combien de tours : ");
  scanf("%d", &t);

  printf("Quel est le nombre initial de cases occupées : ");
  scanf("%d", &c);
*/



  column_width = frame_width / columns;
  row_height = frame_height / rows;



/*
  //SDL_RenderClear(renderer);
  printf("Donner les coordonnées de la première case à placer (type : x, y) : ");
  scanf("%d, %d", &x, &y);
*/

  fenetre = SDL_CreateWindow("Test", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, frame_width, frame_height, 0);
  renderer = SDL_CreateRenderer(fenetre, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
  SDL_RenderFillRect(renderer, &cell);

  SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
  SDL_RenderPresent(renderer); //UPDATE WINDOW

  if(SDL_VideoInit(NULL) < 0) {
      printf("Erreur d'initialisation de la SDL : %s",SDL_GetError());
      return EXIT_FAILURE;
  }

  if(renderer == NULL) {
      printf("Erreur lors de la creation d'un renderer : %s",SDL_GetError());
      return EXIT_FAILURE;
  }

  for(unsigned int col = 0; col < columns; col++){
    SDL_RenderDrawLine(renderer, col * column_width, 0, col * column_width, frame_height - 1);
  }
  for(unsigned int row = 0; row < rows; row++){
    SDL_RenderDrawLine(renderer, 0, row * row_height, frame_width - 1, row * row_height);
  }
  SDL_RenderPresent(renderer);
  SDL_Delay(5000);
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(fenetre);
}
