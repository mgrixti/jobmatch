

class AHP:

    matrix = None


    def GenerateMatrix(self, numCriteria):

        # initialize Matrix to all
        AHP.matrix = [[1 for x in range(numCriteria)] for x in range(numCriteria)]
        #TODO: code

    #def PopulateMatrix(self):



    def CalculateOppositeWeight(self, weight):

        oppositeWeight = 1/weight;

        if oppositeWeight >= 1:

            oppositeWeight = round(oppositeWeight)

        return oppositeWeight