import json
import os
from .puzzle import PicrossPuzzle
from .settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_SELECTED, COLOR_TEXT, FONT_SIZE_HINTS, FONT_SIZE_TEXT, GameSettings
import pygame.gfxdraw
import pygame.font
import copy
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
        self.fileName = solution.getFileName()
        # NOTE this got messed up on doing the gfx stuff, so i need a new matrix to track the true logic positions, no i do not dare to touch the ancient code
        self.localMatrix = []
        self.trueSolution = []
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
        # NOTE deep copy of the just created matrix
        self.trueSolution = copy.deepcopy(self.localMatrix)
        self.lineHints = self.genLineHints()
        self.columnHints = self.genColumnHints()

    def checkMatrixParity(self) -> bool:
        for (solutionLine, localLine) in zip(self.solution, self.trueSolution):
            # I transposed one of the matrices by mistake *sigh*
            for (solutionTerm, localTerm) in zip(solutionLine, localLine):
                if(solutionTerm != localTerm):
                    return False
        return True

    def draw(self, windowRenderer) -> None:
        windowRenderer.getWindow().fill(COLOR_BACKGROUND)

        backText = windowRenderer.getHintFont().render("Back?", True, COLOR_TEXT)
        windowRenderer.getWindow().blit(backText, (20, 20))

        if(not self.checkMatrixParity()):
            localX = self.puzzleArea[0]
            localY = self.puzzleArea[1]
            localXdimension = 0
            localYdimension = 0
            # Size between squares
            verticalSize = int(
                (self.puzzleArea[3] - self.puzzleArea[1]) / self.yDimension)
            horizontalSize = int(
                (self.puzzleArea[2] - self.puzzleArea[0]) / self.xDimension)
            # Final coords
            finalLocalX = localX + (self.xDimension*horizontalSize)
            finalLocalY = localY + (self.yDimension*verticalSize)
            # Draws hints
            textX = self.workingArea[0] + (self.workingArea[0] * 0.8)
            textY = self.workingArea[1] - (self.workingArea[1] * 0.2)
            for hint in self.columnHints:
                hintText = windowRenderer.getHintFont().render(hint, True, COLOR_TEXT)
                windowRenderer.getWindow().blit(hintText, (textX, textY))
                textX += horizontalSize
                pass
            textX = self.workingArea[0]
            textY = self.workingArea[1] + (self.workingArea[1] * 0.8)
            for hint in self.lineHints:
                hintText = windowRenderer.getHintFont().render(hint, True, COLOR_TEXT)
                windowRenderer.getWindow().blit(hintText, (textX, textY))
                textY += verticalSize
                pass
            while(True):
                # Draws from left to right, if the line is done, increment Y and continue drawing
                if(localXdimension >= self.xDimension and localYdimension < self.yDimension):
                    localX = self.puzzleArea[0]
                    localXdimension = 0
                    localY += verticalSize
                    localYdimension += 1
                # If the draw is finished, do the last two lines of the grid
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
                    pygame.gfxdraw.filled_polygon(windowRenderer.getWindow(), [(
                        localX, localY), (localX + horizontalSize, localY), (localX + horizontalSize, localY + verticalSize), (localX, localY + verticalSize)], COLOR_SELECTED)
                    localX += horizontalSize
                    localXdimension += 1
                else:
                    pygame.gfxdraw.line(windowRenderer.getWindow(
                    ), localX, localY, finalLocalX, localY, COLOR_FOREGROUND)
                    pygame.gfxdraw.line(windowRenderer.getWindow(
                    ), localX, localY, localX, finalLocalY, COLOR_FOREGROUND)
                    localX += horizontalSize
                    localXdimension += 1
        else:
            # The player WON
            # TODO save.dat stuff
            winText = windowRenderer.getTextFont().render("YOU WIN!", True, COLOR_TEXT)
            windowRenderer.getWindow().blit(winText, ((int(GameSettings().getResolution(
            )[0])/2) - (3*FONT_SIZE_TEXT), int(GameSettings().getResolution()[1])*0.4))
            dirname = os.path.dirname(__file__)
            filename = dirname[:-8] + '/resources/save.json'
            saveFile = open(filename, "r")
            x = json.loads(saveFile.read())
            saveFile.close()
            if self.fileName not in x["levels"]:
                x["levels"].append(self.fileName)
            # x.update("levels":{self.fileName: True})
                saveFile = open(filename, "w")
                json.dump(x, saveFile, indent=4)
                saveFile.close()
        pass

    def clickHandler(self, x: int, y: int) -> None | str:
        # NOTE back text hack
        if(x >= 20 and x <= 20 + (len("Back?")*FONT_SIZE_HINTS)):
            if(y >= 20 and y <= 20 + FONT_SIZE_HINTS):
                return "PUZZLEBACK"
            pass
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
                    self.trueSolution[clickedSquare[1]][clickedSquare[0]] = 1
                else:
                    self.localMatrix[clickedSquare[0]][clickedSquare[1]] = 0
                    self.trueSolution[clickedSquare[1]][clickedSquare[0]] = 0
                pass
            pass
        return None
        pass

    def genLineHints(self) -> list:
        stringList = []
        for line in self.solution:
            counter = 0
            resultString = ""
            for term in line:
                if(term != 0):
                    counter += 1
                else:
                    if counter > 0:
                        resultString += str(counter) + ' '
                    counter = 0
            if counter > 0:
                resultString += str(counter) + ' '
            stringList.append(resultString)
        return stringList

    def genColumnHints(self) -> list:
        stringList = []

        # NOTE: probable problem when doing non square matrices
        for i in range(len(self.solution)):
            counter = 0
            resultString = ""
            for j in range(len(self.solution[i])):
                if(self.solution[j][i] != 0):
                    counter += 1
                else:
                    if counter > 0:
                        resultString += str(counter) + ' '
                    counter = 0
            if counter > 0:
                resultString += str(counter) + ' '
            stringList.append(resultString)
        return stringList
