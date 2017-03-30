import csv

from overwatch import Hero, Player
from util import assign


def readowcsv(filename):
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
                    continue
                elif item == "✓":
                    player.other_characters.append(hero)
                    pass
                elif item.isdigit():
                    number = int(item)
                    if len(player.priority_list) < number or player.priority_list[number - 1] == None:
                        assign(player.priority_list, number - 1, [])
                    player.priority_list[number - 1].append(hero)
                else:
                    print("Invalid charachter in cell")
    return heroes, players