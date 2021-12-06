from .puzzle import PicrossPuzzle
from .settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_TEXT
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
        for line in solution.getSolution():
            self.yDimension += 1
            # TODO fix this so it accepts non square matrices
            self.xDimension += 1
            localLine = []
            for term in line:
                localLine.append(0)
            self.localMatrix.append(localLine)
        # Grid vertical space in px following (xMax - xMin) / termQty

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
        verticalSize =  int(
            (self.puzzleArea[3] - self.puzzleArea[1]) / self.yDimension)
        horizontalSize =int(
            (self.puzzleArea[2] - self.puzzleArea[0]) / self.xDimension)
        finalLocalX = localX + (self.xDimension*horizontalSize)
        finalLocalY = localY + (self.yDimension*verticalSize)

        while(True):
            if(localXdimension >= self.xDimension and localYdimension >= self.yDimension):
                # pygame.gfxdraw.line(windowRenderer.getWindow(
                # ), localX, self.puzzleArea[0], localX, self.puzzleArea[3], COLOR_FOREGROUND)
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, self.puzzleArea[1], localX, finalLocalY, COLOR_FOREGROUND)
                break
            else:
                if(localXdimension >= self.xDimension):
                    localX = self.puzzleArea[0]
                    localXdimension = 0
                    localY += verticalSize
                    localYdimension += 1
                # FIXME o print ta errado
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, localY, finalLocalX, localY, COLOR_FOREGROUND)
                pygame.gfxdraw.line(windowRenderer.getWindow(
                ), localX, localY, localX, finalLocalY, COLOR_FOREGROUND)
                localX += horizontalSize
                localXdimension += 1
                # localY += self.verticalSize

        pass
