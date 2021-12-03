import matrixIO
import settings

# TODO per-tile RGB values


class PicrossPuzzle:
    def __init__(self, matrix: list) -> None:
        self.solution = matrix
        # NOTE these are coordinates (xMin,yMin,xMax,yMax)
        # NOTE for 640x480 (4:3) there will be no bounding box
        localResolution = settings.GameSettings.getResolution()
        if(localResolution[0] / localResolution[1] == 4/3):
            self.workingArea = (0, 0, 0, 0)
        else:
            self.workingArea = (int(localResolution[0]*0.15), int(localResolution[1]*0.1), int(
                localResolution[0]*0.85), int(localResolution[1]*0.9))

    @classmethod
    def fromFile(self, filename: str) -> None:
        self.solution = matrixIO.readMatrix(filename)
        localResolution = settings.GameSettings.getResolution()
        if(localResolution[0] / localResolution[1] == 4/3):
            self.workingArea = (0, 0, 0, 0)
        else:
            self.workingArea = (int(localResolution[0]*0.15), int(localResolution[1]*0.1), int(
                localResolution[0]*0.85), int(localResolution[1]*0.9))

    def getSolution(self):
        return self.solution

    def writePuzzleToFile(self, filename: str):
        matrixIO.writeMatrix(self.solution, filename)

    def getWorkingArea(self):
        return self.workingArea

    def setWorkingArea(self, workingAreaTuple):
        self.workingArea = workingAreaTuple
