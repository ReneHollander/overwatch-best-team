from util import auto_str


@auto_str
class Player:
    def __init__(self, name, battletag):
        self.name = name
        self.battletag = battletag
        self.weighting = {}

    def __repr__(self):
        return self.battletag

    def weightList(self, composition):
        list = []
        for hero in composition:
            list.append(self.weighting[hero])
        return list


@auto_str
class Hero:
    def __init__(self, name):
        self.name = name

    def simplename(self):
        return self.name.lower().replace(':', '').replace(' ', '-').replace('ö', 'o')

    def __repr__(self):
        return self.name


def matchHeroes(heroes, composition):
    for hero in heroes:
        for i in range(0, len(composition)):
            if composition[i] == hero.name:
                composition[i] = hero


def matchPlayers(players, lineup):
    for player in players:
        for i in range(0, len(lineup)):
            if lineup[i] == player.battletag:
                lineup[i] = player
