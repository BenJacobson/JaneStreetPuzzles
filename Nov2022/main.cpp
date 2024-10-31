#include <cmath>
#include <iostream>
#include <vector>

#include "SDL/include/SDL.h"
#include "pentagon.h"

void search(std::vector<Pentagon> &pentagons) {}

int main() {
  std::vector<Pentagon> pentagons;
  pentagons.push_back({Vec2(0, 0), Vec2(1, 0)});
  search(pentagons);

  // /* Initialises data */
  // SDL_Window *window = NULL;

  // /*
  //  * Initialises the SDL video subsystem (as well as the events subsystem).
  //  * Returns 0 on success or a negative error code on failure using
  //  * SDL_GetError().
  //  */
  // if (SDL_Init(SDL_INIT_VIDEO) != 0) {
  //   fprintf(stderr, "SDL failed to initialise: %s\n", SDL_GetError());
  //   return 1;
  // }

  // /* Creates a SDL window */
  // window =
  //     SDL_CreateWindow("SDL Example",           /* Title of the SDL window */
  //                      SDL_WINDOWPOS_UNDEFINED, /* Position x of the window */
  //                      SDL_WINDOWPOS_UNDEFINED, /* Position y of the window */
  //                      100,  /* Width of the window in pixels */
  //                      100, /* Height of the window in pixels */
  //                      0);     /* Additional flag(s) */

  // /* Checks if window has been created; if not, exits program */
  // if (window == NULL) {
  //   fprintf(stderr, "SDL window failed to initialise: %s\n", SDL_GetError());
  //   return 1;
  // }

  return 0;
}