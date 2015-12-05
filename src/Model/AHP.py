
# Holds all AHP related function
class AHP:

    numCriteria = 5

    # Builds matrix of weights
    # data should be in an array in order of row
    def GenerateMatrix(self, data=[1,1,1,1,1]):

        # initialize Matrix to all 1s
        matrix = [[1 for x in range(AHP.numCriteria)] for x in range(AHP.numCriteria)]
        #TODO: code

        # For each row inset/generate opposite row data
        # todo Fix x advancement
        row = 0

        for y in range(AHP.numCriteria -1):
            x = row
            for x in range(AHP.numCriteria -1):

                if x == y:
                    matrix[x][y] = 1
                else:
                    #Pop next data off stack
                    weight = data.pop(0)
                    matrix[x][y] = weight
                    matrix[y][x] = AHP.CalculateOppositeWeight(self, weight)
            row=+ 1


    def CalculateOppositeWeight(self, weight=1):

        # 1 divided by weight to find the opposite corresponding weight for the matrix
        oppositeWeight = 1/weight;

        # If the oppositeWeight is larger that 1, round to the nearest whole number.
        if oppositeWeight >= 1:

            oppositeWeight = round(oppositeWeight)

        return oppositeWeight