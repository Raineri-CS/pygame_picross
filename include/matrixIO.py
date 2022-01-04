import copy

def readMatrix(filename):
    file = open("./resources/levels/%s" % filename, "r")
    resultMatrix = []
    for line in file:
        resultLine = []
        for term in line:
            if term != "\n":
                resultLine.append(int(term))
        resultMatrix.append(resultLine)
    file.close()
    # NOTE this was not needed, i'll leave the method here anyway
    # resultMatrix = transposeMatrix(resultMatrix)
    return resultMatrix
# TODO check how python deals with relative filepaths


def writeMatrix(matrix, filename):
    file = open("./resources/levels/%s" % filename, "w+")
    for line in matrix:
        for term in line:
            file.write(term)
        file.write("\n")
    return


def transposeMatrix(localMatrix: list) -> list:
    resultMatrix = copy.deepcopy(localMatrix)
    for lineIdx, lineVal in enumerate(localMatrix):
        for termIdx, termVal in enumerate(lineVal):
            resultMatrix[lineIdx][termIdx] = localMatrix[termIdx][lineIdx]
    return resultMatrix
    pass
