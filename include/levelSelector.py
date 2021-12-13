import pygame
import pygame.gfxdraw
from .settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_TEXT, FONT_SIZE_HINTS, GameSettings
from .sceneRenderer import Renderer

SELECTION_BOX_SIZE = 20


class levelSelect():
    def __init__(self) -> None:
        self.levelList = GameSettings().getLevelList()
        pass

    def draw(self, windowRenderer: Renderer) -> None:
        windowRenderer.getWindow().fill(COLOR_BACKGROUND)
        backText = windowRenderer.getHintFont().render("Back?", True, COLOR_TEXT)
        windowRenderer.getWindow().blit(backText, (5, 5))

        arrowLeftText = windowRenderer.getHintFont().render("<", True, COLOR_TEXT)
        arrowRightText = windowRenderer.getHintFont().render(">", True, COLOR_TEXT)

        # Calculate the margins if applicable
        if(int(GameSettings().getResolution()[0]) / int(GameSettings().getResolution()[1]) == 4/3):
            horizontalMargin = (0, int(GameSettings().getResolution()[0]))
            verticalMargin = (25, int(GameSettings().getResolution()[1]))
            # TODO the menu things
            pass
        else:
            horizontalMargin = (int(GameSettings().getResolution()[
                                0]) * 0.1, int(GameSettings().getResolution()[0]) * 0.9)
            verticalMargin = (int(GameSettings().getResolution()[
                              1]) * 0.1, int(GameSettings().getResolution()[1]) * 0.9)
            pass

        # Draw arrows
        # TODO make these conditional so it doesnt show if there isnt any other levels to load in
        windowRenderer.getWindow().blit(
            arrowLeftText, (horizontalMargin[0], int(int(GameSettings().getResolution()[1])/2)))
        windowRenderer.getWindow().blit(arrowRightText,
                                        (horizontalMargin[1] - FONT_SIZE_HINTS, int(int(GameSettings().getResolution()[1])/2)))

        # Draw selection boxes
        self.drawSelectionBox(
            windowRenderer, horizontalMargin[0] + (FONT_SIZE_HINTS * 1.5), verticalMargin[0], True)
        # Each arrow will occupy 7.5% of each side, thus needing the selection boxes to be drawn offset to that proportion

        pass

    def drawSelectionBox(self, windowRenderer: Renderer, x: int, y: int, isComplete: bool):
        # NOTE this should be relative to the res the game is running, but itll have to do for now
        pygame.gfxdraw.rectangle(
            windowRenderer.getWindow(), (x, y, x+SELECTION_BOX_SIZE, y+SELECTION_BOX_SIZE), COLOR_FOREGROUND)
        # FIXME coordinates
        if(isComplete):
            vText = windowRenderer.getHintFont().render("V", True, COLOR_TEXT)
            windowRenderer.getWindow().blit(
                vText, (x+SELECTION_BOX_SIZE-FONT_SIZE_HINTS, y+(SELECTION_BOX_SIZE/2)))
            pass
        else:
            xText = windowRenderer.getHintFont().render("X", True, COLOR_TEXT)
            windowRenderer.getWindow().blit(
                xText, (x+(SELECTION_BOX_SIZE/2) - FONT_SIZE_HINTS, y+(SELECTION_BOX_SIZE/2)))
            pass
        pass

    def clickHandler(self, x: int, y: int) -> None:
        # TODO
        pass
