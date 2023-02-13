#include <stdio.h>
#include <stdlib.h>
#include <SDL2/SDL.h>


int main(void){
  fenetre = SDL_CreateWindow("Une fenetre SDL" , SDL_WINDOW_FULLSCREEN_DESKTOP , SDL_WINDOW_FULLSCREEN , frame_width , frame_height , 0);

  // Si la fenetre n'a pas pu etre cree, le programme ne peut continuer
  if(fenetre == NULL) {
      printf("Erreur lors de la creation d'une fenetre : %s",SDL_GetError());
      return EXIT_FAILURE;
  }

  // Création du renderer
  // Le renderer est l'objet qui permet de dessiner dans la fenetre.
  // la fonction de creation du renderer renvoie NULL si le renderer n'a pu etre cree
  renderer = SDL_CreateRenderer(fenetre, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC); // Création du renderer

  // Si le renderer n'a pu etre creer, le programme ne peut pas continuer
  if(renderer == NULL) {
      printf("Erreur lors de la creation d'un renderer : %s",SDL_GetError());
      return EXIT_FAILURE;
  }
  SDL_Delay(15000); // Pause de 2 secondes, pour admirer notre œuvre autant que l'on veut


  // Destruction du renderer et de la fenêtre :
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(fenetre);
  SDL_Quit(); // On quitte la SDL
}
