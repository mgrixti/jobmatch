

class AHP:

    numCriteria = 5

    def GenerateMatrix(self, data=[1,1,1,1,1]):

        # initialize Matrix to all 1s
        matrix = [[1 for x in range(AHP.numCriteria)] for x in range(AHP.numCriteria)]
        #TODO: code

        for y in range(AHP.numCriteria):
            for x in range(AHP.numCriteria):
                if x == y:
                    matrix[x][y] = 1
                else:
                    data.pop(0)






    def CalculateOppositeWeight(self, weight):

        # 1 divided by weight to find the opposite corresponding weight for the matrix
        oppositeWeight = 1/weight;

        # If the oppositeWeight is larger that 1, round to the nearest whole number.
        if oppositeWeight >= 1:

            oppositeWeight = round(oppositeWeight)

        return oppositeWeight