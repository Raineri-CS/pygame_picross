from .settings import GameSettings
import pygame
pygame.init()


class Renderer:
    def __init__(self) -> None:
        self.windowSize = GameSettings().getResolution()
        for i in range(len(self.windowSize)):
            self.windowSize[i] = int(self.windowSize[i])
        self.window = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption("Pygame Picross")

    def getWindow(self):
        return self.window

    def swapBuffer(self):
        pygame.display.flip()
