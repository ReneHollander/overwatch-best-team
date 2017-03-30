import munkres
from munkres import Munkres

from input import readowcsv
from overwatch import matchHeroes, matchPlayers

heroes, players = readowcsv('Overwatch Cup - Hero Preferences.csv', 1 / 4)

# composition = ["Ana", "Lucio", "Reinhardt", "Zarya", "Tracer", "Soldier: 76"]
# composition = ["Tracer", "Soldier: 76", "Winston", "Zarya", "Lucio", "Zenyatta"]
composition = ["Soldier: 76", "Roadhog", "Reinhardt", "Zarya", "Ana", "Lucio"]
# composition = ["Pharah", "Mercy", "Reinhardt", "Zarya", "Soldier: 76", "Lucio"]
lineup = ["Ra4#2632", "TheKillerKuh#2662", "potatoboy#2111", "Backfish#2465", "Rene8888#21258", "Windbreaker#2639"]

matchHeroes(heroes, composition)
matchPlayers(players, lineup)

print("heroes=" + str(heroes))
print("players=" + str(players))
print("composition=" + str(composition))
print("lineup=" + str(lineup))


def buildMatrix(lineup, composition):
    mat = []
    for player in lineup:
        mat.append(player.weightList(composition))
    return mat


m = Munkres()

matrix = buildMatrix(lineup, composition)
cost_matrix = munkres.make_cost_matrix(matrix, lambda cost: int(100 - (cost * 100)))
indexes = m.compute(cost_matrix)

picks = {}

for index in indexes:
    picks[lineup[index[0]]] = composition[index[1]]

print(picks)
