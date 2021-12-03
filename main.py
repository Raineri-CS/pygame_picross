from pygame.constants import K_ESCAPE, KEYDOWN, KEYUP, MOUSEBUTTONUP
# TODO remove
from include.puzzle import PicrossPuzzle
from include.sceneRenderer import Renderer
import pygame

from include.gameCoordinator import GameCoordinator


def main():
    EXIT = False
    windowRenderer = Renderer()
    # TODO remove
    currentScreen = GameCoordinator(PicrossPuzzle(None, "1"))
    clock = pygame.time.Clock()
    while not EXIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EXIT = True
            elif event.type == KEYDOWN:
                # TODO Do stuff
                print("lol")
            elif event.type == KEYUP:
                if(event.key == K_ESCAPE):
                    EXIT = True
            elif event.type == MOUSEBUTTONUP:
                # TODO Do click stuff
                currentScreen.draw(windowRenderer)
        clock.tick(30)
        windowRenderer.swapBuffer()
    pygame.quit()


if __name__ == "__main__":
    main()
