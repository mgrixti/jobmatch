from src.Model.AHP import AHP


def test_ahp():


    ahp = AHP()
    data = [3,7,5,1,9,3,9,5,7,5]
    matrix = ahp.generateMatrix(data)

    for y in range(5):
        row = ""
        for x in range(5):
            row += str(matrix[y][x])
            row += ' '


    weights = ahp.generateWeights(matrix)

    sumWeights = 0
    for x in range(5):
        sumWeights+= weights[x]

    assert sumWeights == 1

