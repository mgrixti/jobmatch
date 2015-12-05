
# Holds all AHP related function
class AHP:


    numCriteria = 5

    # Builds matrix of weights
    # data should be in an array in order of row
    def GenerateMatrix(self, data=[3,0.3,9,3,3,7,3,3,3,5]):

        # initialize Matrix to all 1s
        matrix = [[1 for x in range(AHP.numCriteria)] for x in range(AHP.numCriteria)]
        #TODO: code

        # For each row inset/generate opposite row data
        # todo Fix x advancement

        # Nested loops enter data for top half of matrix and generates for bottom half
        # x = original data, g = generate data
        #   1 x x
        #   g 1 x
        #   g g 1
        for y in range(AHP.numCriteria):

            for x in range(y, AHP.numCriteria):
                #
                if x == 0:
                    x = y

                                # if x and y match they are the same criteria and have an equal weighting of 1
                if x == y:
                    matrix[x][y] = 1
                else:
                    #Pop next data off stack
                    weight = data.pop(0)
                    matrix[x][y] = weight
                    matrix[y][x] = AHP.CalculateOppositeWeight(self, weight)

        return matrix

    # Helper method for matrix generation
    # Generates the opposite value of the weight handed in.
    def CalculateOppositeWeight(self, weight=1):

        # 1 divided by weight to find the opposite corresponding weight for the matrix
        oppositeWeight = 1/weight;

        # If the oppositeWeight is larger that 1, round to the nearest whole number.
        if oppositeWeight >= 1:

            oppositeWeight = round(oppositeWeight)

        return oppositeWeight