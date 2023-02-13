#include <SDL2/SDL.h>
#include <stdlib.h>
#include <stdio.h>


unsigned int frame_width = 500;
unsigned int frame_height = 500;


int main(int argc, char* argv){
  
  printf("Nombre de lignes : ");
  scanf("%d", &rows);

  printf("Nombre de colonnes : ");
  scanf("%d", &columns);
  // Initialize SDL
  SDL_Init(SDL_INIT_VIDEO);

  //Create SDL Window
  SDL_Window *fenetre = SDL_CreateWindow("Test SDL2", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, frame_width, frame_height, SDL_WINDOW_OPENGL);

  // Create SDL renderer (accelerated and sync with the display refresh rate)
  SDL_Renderer *renderer = SDL_CreateRenderer(fenetre, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);


  int run = 1; // True
  SDL_Event event;

  while(run){
    while(SDL_PollEvent(&event)){
      if(event.type = SDL_Quit){
        run = 0;
      }
    }
    // Clear Screen (GAME LOOP)
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    //Draw
    SDL_SetRenderDrawColor(renderer, 127, 0, 255, 255);
    SDL_RenderDrawLine(renderer, 100, 100);
    //Buff
    SDL_RenderPresent(renderer);
  }
  // delay
  SDL_Delay(5000);
  // Release ressources
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(fenetre);
  SDL_Quit();
}
