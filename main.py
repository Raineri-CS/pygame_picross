from pygame.constants import K_ESCAPE, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from include.levelSelector import levelSelect
# TODO remove
from include.puzzle import PicrossPuzzle
from include.mainMenu import MainMenu
from include.sceneRenderer import Renderer
from include.musicPlayer import MusicPlayer
import pygame

from include.gameCoordinator import GameCoordinator
from include.settings import SONG_OVER


def main():
    EXIT = False
    windowRenderer = Renderer()
    # TODO remove
    # currentScreen = GameCoordinator(PicrossPuzzle(None, "1"))
    currentScreen = MainMenu()
    currentScreen.draw(windowRenderer)
    clock = pygame.time.Clock()
    localMusicPlayer = MusicPlayer()
    while not EXIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                EXIT = True
            elif event.type == KEYUP:
                if(event.key == K_ESCAPE):
                    EXIT = True
            elif event.type == MOUSEBUTTONDOWN:
                localMusicPlayer.click()
                retVal = currentScreen.clickHandler(pygame.mouse.get_pos()[
                    0], pygame.mouse.get_pos()[1])
                # NOTE thanks for no switch cases python =)))))
                if(retVal != None):
                    # NOTE this is also a hack so i dont have to refactor a good chunk of the code
                    if(retVal == "PLAY" or retVal == "PUZZLEBACK"):
                        currentScreen = levelSelect()
                        pass
                    elif(retVal[:len("SELECT ")] == "SELECT "):
                        currentScreen = GameCoordinator(
                            PicrossPuzzle(None, retVal[len("SELECT "):]))
                        pass
                    elif(retVal == "LVLSELECTBACK"):
                        currentScreen = MainMenu()
                        pass
                    pass
                currentScreen.draw(windowRenderer)
            elif event.type == SONG_OVER:
                localMusicPlayer.swapTracks()
        clock.tick(30)
        windowRenderer.swapBuffer()
    # Destructors
    if pygame.font.get_init():
        pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
