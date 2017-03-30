import munkres
from munkres import Munkres

from compositionbuilder import calculateIdealComposition
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

picks = calculateIdealComposition(lineup, composition)

print("picks=" +str(picks))
