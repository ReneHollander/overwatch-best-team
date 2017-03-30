from input import readowcsv

def countNone(dict):
    cnt = 0
    for key, value in dict.items():
        if value == None:
            cnt += 1
    return cnt

def getNone(dict):
    for key, value in dict.items():
        if value == None:
            return key

def isPicked(hero, picks):
    for key, value in picks.items():
        if value == hero:
            return True
    return False

heroes, players = readowcsv('Overwatch Cup - Hero Preferences.csv')

optioncount = 4

# composition = ["Ana", "Lucio", "Reinhardt", "Zarya", "Tracer", "Soldier: 76"]
# composition = ["Tracer", "Soldier: 76", "Winston", "Zarya", "Lucio", "Zenyatta"]
# composition = ["Soldier: 76", "Roadhog", "Reinhardt", "Zarya", "Ana", "Lucio"]
composition = ["Pharah", "Mercy", "Reinhardt", "Zarya", "Soldier: 76", "Lucio"]
lineup = ["Ra4#2632", "TheKillerKuh#2662", "potatoboy#2111", "Backfish#2465", "Rene8888#21258", "Windbreaker#2639"]
picks = {}

for hero in heroes:
    for i in range(0, len(composition)):
        if composition[i] == hero.name:
            composition[i] = hero

for player in players:
    player.buildWeighting(1 / optioncount, heroes)
    for i in range(0, len(lineup)):
        if lineup[i] == player.battletag:
            lineup[i] = player

for player in lineup:
    picks[player] = None

print("heroes=" + str(heroes))
print("players=" + str(players))
print("composition=" + str(composition))
print("lineup=" + str(lineup))
print("picks=" + str(picks))

def getOtherPick(hero, picks):
    for key, value in picks.items():
        if value != None and value[0] == hero:
            return key, value[0], value[1]
    return None

while countNone(picks) >= 1:
    p = getNone(picks)
    possible = p.allFromPool(composition)
    for hero, weight in possible:
        otherPick = getOtherPick(hero, picks)
        if otherPick == None:
            picks[p] = (hero, weight)
        elif otherPick[2] <= weight:
            picks[otherPick[0]] = None
            picks[p] = (hero, weight)
    print(picks)

print("picks=" + str(picks))