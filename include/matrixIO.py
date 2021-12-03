def readMatrix(filename):
    file = open("./resources/levels/%s" % filename, "r")
    resultMatrix = []
    for line in file:
        resultLine = []
        for term in line:
            resultLine.insert(term)
        resultMatrix.append(resultLine)
    file.close()
    return resultMatrix
# TODO check how python deals with relative filepaths


def writeMatrix(matrix, filename):
    file = open("./resources/levels/%s" % filename, "w+")
    for line in matrix:
        for term in line:
            file.write(term)
        file.write("\n")
    return
