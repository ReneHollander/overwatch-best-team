import csv

from overwatch import Hero, Player


def readowcsv(filename, gradient):
    heroes = []
    players = []
    with open(filename, 'rt', encoding='utf-8') as csvfile:
        overwatchcsv = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = overwatchcsv.__next__()
        for item in header:
            if item != "Heroes":
                info = item.split("\n")
                players.append(Player(info[0], info[1]))
        for row in overwatchcsv:
            if row[0] == "":
                break
            hero = Hero(row[0])
            heroes.append(hero)
            for i in range(1, len(players) + 1):
                player = players[i - 1]
                item = row[i]
                if item == "":
                    player.weighting[hero] = 0
                elif item == "✓":
                    player.weighting[hero] = gradient
                elif item.isdigit():
                    player.weighting[hero] = float(1 - ((int(item) - 1) * gradient))
                else:
                    print("Invalid charachter in cell")
    return heroes, players
