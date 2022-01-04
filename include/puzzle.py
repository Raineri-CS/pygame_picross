from .matrixIO import readMatrix, writeMatrix
from .settings import GameSettings

# TODO per-tile RGB values


class PicrossPuzzle:
    def __init__(self, matrix: list = None, filename: str = None) -> None:
        if matrix:
            self.fileName = ''
            self.solution = matrix
            # NOTE these are coordinates (xMin,yMin,xMax,yMax)
            # NOTE for 640x480 (4:3) there will be no bounding box
            localResolution = GameSettings().getResolution()
            # TODO test this
            if(localResolution[0] / localResolution[1] == 4/3):
                self.workingArea = (0, 0, 0, 0)
                self.puzzleArea = (
                    int(localResolution[0] * 1.4), int(localResolution[1] * 1.4), int(localResolution[0]), int(localResolution[1]))
            else:
                self.workingArea = (int(localResolution[0]*0.15), int(localResolution[1]*0.1), int(
                    localResolution[0]*0.85), int(localResolution[1]*0.9))
                self.puzzleArea = (
                    int(self.workingArea[0] * 1.4), int(self.workingArea[1] * 1.4), int(self.workingArea[2]), int(self.workingArea[3]))
        elif filename:
            self.fileName = filename
            self.solution = readMatrix(filename)
            localResolution = GameSettings().getResolution()
            if(int(localResolution[0]) / int(localResolution[1]) == 4/3):
                self.workingArea = (0, 0, 0, 0)
                self.puzzleArea = (
                    int(localResolution[0] * 1.4), int(localResolution[1] * 1.4), int(localResolution[0]), int(localResolution[1]))
            else:
                self.workingArea = (int(int(localResolution[0])*0.15), int(int(localResolution[1])*0.1), int(
                    int(localResolution[0])*0.85), int(int(localResolution[1])*0.9))
                self.puzzleArea = (
                    int(self.workingArea[0] * 1.4), int(self.workingArea[1] * 1.4), int(self.workingArea[2]), int(self.workingArea[3]))

    def getSolution(self):
        return self.solution

    def writePuzzleToFile(self, filename: str):
        writeMatrix(self.solution, filename)

    def getWorkingArea(self):
        return self.workingArea

    def setWorkingArea(self, workingAreaTuple):
        self.workingArea = workingAreaTuple

    def getPuzzleArea(self):
        return self.puzzleArea

    def getFileName(self) -> str:
        return self.fileName