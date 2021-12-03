import puzzle
from settings import COLOR_BACKGROUND, COLOR_FOREGROUND, COLOR_TEXT

# Basically the scene with the gameplay stuff in it
# What does it do?
#   Draws its own scene (Flipping the frames will happen on the main routine)
#   Checks for win condition
#   Stores the localGame matrix
#   Goes back to the level select on back click
#   Sets the map as completed if win


class GameCoordinator():
    def __init__(self, solution: puzzle) -> None:
        self.solution = solution.getSolution()
        self.workingArea = solution.getWorkingArea()
        self.localMatrix = []
        # Build a similarly dimensioned matrix
        for line in solution.getSolution():
            localLine = []
            for term in line:
                localLine.insert(0)
            self.localMatrix.append(localLine)
        

    def checkMatrixParity(self):
        for solutionLine, localLine in self.solution, self.localMatrix:
            for solutionTerm, localTerm in solutionLine, localLine:
                if(solutionTerm != localTerm):
                    return False
        return True

    def draw(self):
        
        pass
