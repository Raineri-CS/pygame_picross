import os
import pygame
from pygame.display import init
import pygame.gfxdraw
from .settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_TEXT, GameSettings
from .sceneRenderer import Renderer

PLAY_BUTTON_WIDTH = 150
PLAY_BUTTON_HEIGHT = 75


class MainMenu():
    def __init__(self) -> None:
        self.clickableEntities = []
        # Main play button
        self.clickableEntities.append(((int(GameSettings().getResolution()[0])/2) - (PLAY_BUTTON_WIDTH/2), int(GameSettings().getResolution()[
                                      1]) * 0.6, (int(GameSettings().getResolution()[0])/2) + (PLAY_BUTTON_WIDTH/2), (int(GameSettings().getResolution()[1]) * 0.6) + PLAY_BUTTON_HEIGHT))

        pass

    def draw(self, windowRenderer: Renderer) -> None:
        playText = windowRenderer.getTextFont().render("PLAY", True, COLOR_TEXT)
        windowRenderer.getWindow().fill(COLOR_BACKGROUND)

        dirname = os.path.dirname(__file__)
        filename = dirname[:-8] + '/resources/sprites/Pycross_titlecard.png'
        titleCard = pygame.image.load(filename)

        pygame.gfxdraw.rectangle(windowRenderer.getWindow(), pygame.Rect((int(GameSettings().getResolution()[0])/2) - (PLAY_BUTTON_WIDTH/2), int(GameSettings().getResolution()[
            1]) * 0.6, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT), COLOR_FOREGROUND)

        windowRenderer.getWindow().blit(playText, ((int(GameSettings().getResolution()[0])/2) - (PLAY_BUTTON_WIDTH/2) + 24, 12 + int(GameSettings().getResolution()[
            1]) * 0.6))

        windowRenderer.getWindow().blit(
            titleCard, (int(GameSettings().getResolution()[0])*0.2, int(GameSettings().getResolution()[1])*0.1))

        pass

    def clickHandler(self, x: int, y: int) -> None | str:
        for val in self.clickableEntities:
            if(val[0] <= x and val[2] >= x):
                if(val[1] <= y and val[3] >= y):
                    return "PLAY"
            pass
        pass
        return None
