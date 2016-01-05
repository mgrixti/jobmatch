
# Holds all AHP related function
class AHP:


    numCriteria = 5

    # Builds matrix of weights
    # data should be in an array with the data in order of row
    # WORKS
    def generateMatrix(self, data):

        # initialize Matrix to all 1s
        matrix = [[1 for x in range(self.numCriteria)] for x in range(self.numCriteria)]


        # Nested loops enter data for top half of matrix and generates for bottom half
        # x = original data, g = generate data
        #   1 x x
        #   g 1 x
        #   g g 1
        for y in range(self.numCriteria):
            for x in range(y, self.numCriteria):
               # if x and y match they are the same criteria and have an equal weighting of 1
                if x == y:
                    matrix[x][y] = 1
                else:
                    #Pop next data off stack
                    weight = data.pop(0)
                    matrix[y][x] = weight # add weight to matrix
                    matrix[x][y] = self.calculateOppositeWeight(weight) # Generate weight for opposite field

        return matrix

    # Helper method for matrix generation
    # Generates the opposite value of the weight handed in.
    # WORKS
    def calculateOppositeWeight(self, weight=1):

        # 1 divided by weight to find the opposite corresponding weight for the matrix
        oppositeWeight = 1/weight

        # If the oppositeWeight is larger that 1, round to the nearest whole number.
        if oppositeWeight >= 1:

            oppositeWeight = round(oppositeWeight)

        return oppositeWeight

    #
    # sums the columns of the matrix
    # helper method for generateWeights()
    # returns array in order of  columns
    # WORKS
    def sumColumns(self, matrix):

        columnSums=[]

        # sum the columns of the matrix
        for x in range(self.numCriteria):
            sum = 0

            for y in range(self.numCriteria):
                sum+= matrix[y][x]

            columnSums.append(sum)

        return columnSums


    # Generates the weights of each criteria
    #
    def generateWeights(self, matrix):

        columnSums = self.sumColumns(matrix)
        weights = []

        # generates the weighted value of each item in the matrix. WORKS
        for y in range(self.numCriteria):
            for x in range(self.numCriteria):

                matrix[y][x] = matrix[y][x]/columnSums[x]

        # generates the weights of each criteria
        for y in range(self.numCriteria):
            sum = 0

            # adds each item in the row to sum
            for x in range(self.numCriteria):
                sum += matrix[y][x]

            # average of weights
            avg = sum/self.numCriteria

            # adds avg to array of weights
            weights.append(avg)

        return weights
