from .puzzle import PicrossPuzzle
from .settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_SELECTED, COLOR_TEXT
import pygame.gfxdraw
from .sceneRenderer import Renderer

# Basically the scene with the gameplay stuff in it
# What does it do?
#   Draws its own scene (Flipping the frames will happen on the main routine)
#   Checks for win condition
#   Stores the localGame matrix
#   Goes back to the level select on back click
#   Sets the map as completed if win


class GameCoordinator():
    def __init__(self, solution: PicrossPuzzle) -> None:
        self.solution = solution.getSolution()
        self.workingArea = solution.getWorkingArea()
        self.puzzleArea = solution.getPuzzleArea()
        self.localMatrix = []
        # Build a similarly dimensioned matrix
        self.xDimension = 0
        self.yDimension = 0
        # TODO clicked boxes
        for line in solution.getSolution():
            self.yDimension += 1
            # TODO fix this so it accepts non square matrices
            self.xDimension += 1
            localLine = []
            for term in line:
                localLine.append(0)
            self.localMatrix.append(localLine)
        # Grid vertical space in px following (xMax - xMin) / termQty
        self.coordMap = []

    def checkMatrixParity(self):
        for solutionLine, localLine in self.solution, self.localMatrix:
            for solutionTerm, localTerm in solutionLine, localLine:
                if(solutionTerm != localTerm):
                    return False
        return True

    def draw(self, windowRenderer):
        windowRenderer.getWindow().fill(COLOR_BACKGROUND)
        localX = self.puzzleArea[0]
        localY = self.puzzleArea[1]
        localXdimension = 0
        localYdimension = 0
        verticalSize = int(
            (self.puzzleArea[3] - self.puzzleArea[1]) / self.yDimension)
        horizontalSize = int(
            (self.puzzleArea[2] - self.puzzleArea[0]) / self.xDimension)
        finalLocalX = localX + (self.xDimension*horizontalSize)
        finalLocalY = localY + (self.yDimension*verticalSize)
        while(True):
            if(localXdimension >= self.xDimension and localYdimension < self.yDimension):
                localX = self.puzzleArea[0]
                localXdimension = 0
                localY += verticalSize
                localYdimension += 1
            if(localXdimension >= self.xDimension or localYdimension >= self.yDimension):
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), finalLocalX, self.puzzleArea[1], finalLocalX, finalLocalY, COLOR_FOREGROUND)
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), self.puzzleArea[0], localY, finalLocalX, localY, COLOR_FOREGROUND)
                break
            elif (self.localMatrix[localXdimension][localYdimension] == 1):
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, localY, finalLocalX, localY, COLOR_FOREGROUND)
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, localY, localX, finalLocalY, COLOR_FOREGROUND)
                #  TODO test this
                pygame.gfxdraw.rectangle(
                    windowRenderer.getWindow(), (localX, localY, finalLocalX, finalLocalY), COLOR_SELECTED)
                localX += horizontalSize
                localXdimension += 1
            else:
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, localY, finalLocalX, localY, COLOR_FOREGROUND)
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, localY, localX, finalLocalY, COLOR_FOREGROUND)
                localX += horizontalSize
                localXdimension += 1
        pass

    def slotFill(self, x: int, y: int):
        if (self.puzzleArea[0] <= x and self.puzzleArea[2] >= x):
            if (self.puzzleArea[1] <= y and self.puzzleArea[3] >= y):
                verticalSize = int(
                    (self.puzzleArea[3] - self.puzzleArea[1]) / self.yDimension)
                horizontalSize = int(
                    (self.puzzleArea[2] - self.puzzleArea[0]) / self.xDimension)
                clickedSquare = (
                    (int((x - self.puzzleArea[0])/horizontalSize)), int((y - self.puzzleArea[1])/verticalSize))
                if (self.localMatrix[clickedSquare[0]][clickedSquare[1]] == 0):
                    self.localMatrix[clickedSquare[0]][clickedSquare[1]] = 1
                else:
                    self.localMatrix[clickedSquare[0]][clickedSquare[1]] = 0
                pass
            pass
        pass
