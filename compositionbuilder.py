import munkres
from munkres import Munkres


def buildMatrix(lineup, composition):
    mat = []
    for player in lineup:
        mat.append(player.weightList(composition))
    return mat


def calculateIdealComposition(lineup, composition):
    m = Munkres()

    matrix = buildMatrix(lineup, composition)
    cost_matrix = munkres.make_cost_matrix(matrix, lambda cost: int(100 - (cost * 100)))
    indexes = m.compute(cost_matrix)

    picks = []

    for index in indexes:
        picks.append((lineup[index[0]], composition[index[1]]))

    return picks