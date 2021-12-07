from .settings import FONT_SIZE_HINTS, FONT_SIZE_TEXT, GameSettings
import pygame
import os
pygame.init()


class Renderer:
    def __init__(self) -> None:
        self.windowSize = GameSettings().getResolution()
        for i in range(len(self.windowSize)):
            self.windowSize[i] = int(self.windowSize[i])
        self.window = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption("Pygame Picross")
        if pygame.font.get_init():
            pygame.font.init()
        dirname = os.path.dirname(__file__)
        filename = dirname[:-8] + '/resources/fonts/FreeSansBold.otf'
        self.textFont = pygame.font.Font(filename,FONT_SIZE_TEXT)
        self.hintFont = pygame.font.Font(filename,FONT_SIZE_HINTS)

    def getWindow(self):
        return self.window

    def getHintFont(self):
        return self.hintFont

    def getTextFont(self):
        return self.textFont

    def swapBuffer(self):
        pygame.display.flip()
