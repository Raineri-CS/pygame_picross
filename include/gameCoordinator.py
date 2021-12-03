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
        self.localMatrix = []
        # Build a similarly dimensioned matrix
        xDimension = 0
        yDimension = 0
        for line in solution.getSolution():
            yDimension += 1
            localLine = []
            for term in line:
                localLine.append(0)
                xDimension += 1
            self.localMatrix.append(localLine)
        # Grid vertical space in px following (xMax - xMin) / termQty
        self.verticalSize = int(
            (self.workingArea[2] - self.workingArea[0]) / xDimension)
        self.horizontalSize = int(
            (self.workingArea[3] - self.workingArea[1]) / yDimension)

    def checkMatrixParity(self):
        for solutionLine, localLine in self.solution, self.localMatrix:
            for solutionTerm, localTerm in solutionLine, localLine:
                if(solutionTerm != localTerm):
                    return False
        return True

    def draw(self,windowRenderer):
        pygame.gfxdraw.line(windowRenderer.getWindow(
        ), self.workingArea[0], self.workingArea[1], self.workingArea[2], self.workingArea[3], COLOR_FOREGROUND)
        pass
