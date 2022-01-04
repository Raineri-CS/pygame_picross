import pygame
import pygame.gfxdraw
from .settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_TEXT, FONT_SIZE_HINTS, GameSettings
from .sceneRenderer import Renderer

SELECTION_BOX_WIDTH = 150
SELECTION_BOX_HEIGHT = 75
PUZZLES_PER_LINE = 5
PUZZLES_PER_PAGE = PUZZLES_PER_LINE * 5
PUZZLE_MARGIN = 30


class levelSelect():
    def __init__(self) -> None:
        self.levelList = GameSettings().getLevelList()
        self.completedLevelList = GameSettings().getCompletedLevelList()
        self.clickableEntities = []
        self.pageOffset = 0
        # Calculate the margins if applicable
        if(int(GameSettings().getResolution()[0]) / int(GameSettings().getResolution()[1]) == 4/3):
            self.horizontalMargin = (0, int(GameSettings().getResolution()[0]))
            self.verticalMargin = (25, int(GameSettings().getResolution()[1]))
            # TODO the menu things
            pass
        else:
            self.horizontalMargin = (int(GameSettings().getResolution()[
                0]) * 0.1, int(GameSettings().getResolution()[0]) * 0.9)
            self.verticalMargin = (int(GameSettings().getResolution()[
                1]) * 0.1, int(GameSettings().getResolution()[1]) * 0.9)
            pass
        pass

    def draw(self, windowRenderer: Renderer) -> None:
        windowRenderer.getWindow().fill(COLOR_BACKGROUND)
        backText = windowRenderer.getHintFont().render("Back?", True, COLOR_TEXT)
        windowRenderer.getWindow().blit(backText, (20, 20))

        arrowLeftText = windowRenderer.getHintFont().render("<", True, COLOR_TEXT)
        arrowRightText = windowRenderer.getHintFont().render(">", True, COLOR_TEXT)

        # Draw arrows
        # TODO make these conditional so it doesnt show if there isnt any other levels to load in
        # Left arrow
        if(self.pageOffset > 0):
            windowRenderer.getWindow().blit(
                arrowLeftText, (self.horizontalMargin[0], int(int(GameSettings().getResolution()[1])/2)))
            pass
        elif(self.pageOffset + PUZZLES_PER_PAGE < len(self.levelList)):
            windowRenderer.getWindow().blit(arrowRightText,
                                            (self.horizontalMargin[1] - FONT_SIZE_HINTS, int(int(GameSettings().getResolution()[1])/2)))
            pass

        # Each arrow will occupy 7.5% of each side, thus needing the selection boxes to be drawn offset to that proportion
        horizontalOffset = self.horizontalMargin[0] + FONT_SIZE_HINTS * 1.5
        verticalOffset = self.verticalMargin[0]

        # self.drawSelectionBox(
        #     windowRenderer, horizontalOffset, verticalOffset, True)

        # if(len(self.levelList[pageOffset:]) > PUZZLES_PER_LINE):
        # TODO this should increment or decrement based on the arrowClick
        # self.pageOffset = self.pageOffset + PUZZLES_PER_LINE
        # Draw a puzzle line
        # FIXME this
        localPuzzleAmount = 0
        for puzzle in self.levelList[self.pageOffset:self.pageOffset + PUZZLES_PER_PAGE]:
            if(localPuzzleAmount == PUZZLES_PER_LINE):
                verticalOffset = verticalOffset + PUZZLE_MARGIN + SELECTION_BOX_HEIGHT
                horizontalOffset = self.horizontalMargin[0] + \
                    FONT_SIZE_HINTS * 1.5
                localPuzzleAmount = 0
                pass
            if puzzle in self.completedLevelList:
                self.drawSelectionBox(
                    windowRenderer, horizontalOffset, verticalOffset, SELECTION_BOX_WIDTH, SELECTION_BOX_HEIGHT, True)
            else:
                self.drawSelectionBox(
                    windowRenderer, horizontalOffset, verticalOffset, SELECTION_BOX_WIDTH, SELECTION_BOX_HEIGHT, False)

            self.clickableEntities.append(
                (horizontalOffset, verticalOffset, horizontalOffset + SELECTION_BOX_WIDTH, verticalOffset + SELECTION_BOX_HEIGHT))
            horizontalOffset = horizontalOffset + PUZZLE_MARGIN + SELECTION_BOX_WIDTH
            localPuzzleAmount = localPuzzleAmount+1

        #     pass
        # else:
        #     pass
        pass

    def drawSelectionBox(self, windowRenderer: Renderer, x: int, y: int, width: int, height: int, isComplete: bool):
        # NOTE this should be relative to the res the game is running, but itll have to do for now
        pygame.gfxdraw.rectangle(
            windowRenderer.getWindow(), pygame.Rect(x, y, width, height), COLOR_FOREGROUND)
        if(isComplete):
            vText = windowRenderer.getHintFont().render("V", True, COLOR_TEXT)
            windowRenderer.getWindow().blit(
                vText, ((x+(SELECTION_BOX_WIDTH*0.5)) - (FONT_SIZE_HINTS/2),  (y) + FONT_SIZE_HINTS))
            pass
        else:
            xText = windowRenderer.getHintFont().render("X", True, COLOR_TEXT)
            windowRenderer.getWindow().blit(
                xText, ((x+(SELECTION_BOX_WIDTH*0.5)) - (FONT_SIZE_HINTS/2),  (y) + FONT_SIZE_HINTS))
            pass
        pass

    def clickHandler(self, x: int, y: int) -> None | str:
        # TODO back button
        if(x >= 20 and x <= 20 + (len("Back?")*FONT_SIZE_HINTS)):
            if(y >= 20 and y <= 20 + FONT_SIZE_HINTS):
                return "LVLSELECTBACK"
            pass
        # TODO create a proper arrow class so it can be its own thing, instead of this hack
        # left arrow
        if(x >= self.horizontalMargin[0] and x <= self.horizontalMargin[0] + FONT_SIZE_HINTS):
            if(y >= int(int(GameSettings().getResolution()[1])/2) and y <= int(int(GameSettings().getResolution()[1])/2)+FONT_SIZE_HINTS):
                self.pageOffset = self.pageOffset - PUZZLES_PER_PAGE
                self.clickableEntities.clear()
                pass
            pass
        # right arrow
        if(x >= self.horizontalMargin[1] - FONT_SIZE_HINTS and x <= self.horizontalMargin[1] + FONT_SIZE_HINTS):
            if(y >= int(int(GameSettings().getResolution()[1])/2) and y <= int(int(GameSettings().getResolution()[1])/2)+FONT_SIZE_HINTS):
                self.pageOffset = self.pageOffset + PUZZLES_PER_PAGE
                self.clickableEntities.clear()
                pass
            pass

        for idx, val in enumerate(self.clickableEntities):
            if(val[0] <= x and val[2] >= x):
                if(val[1] <= y and val[3] >= y):
                    # It means it "hit" a puzzle to be selected
                    # TODO
                    return "SELECT " + self.levelList[self.pageOffset + idx]
                    pass
            pass

        return None
        pass
