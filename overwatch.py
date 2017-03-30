from util import auto_str


@auto_str
class Player:
    def __init__(self, name, battletag):
        self.name = name
        self.battletag = battletag
        self.priority_list = []
        self.other_characters = []

    def __repr__(self):
        return self.battletag

    def allFromPool(self, pool):
        all = []
        for hero, weight in self.weighting.items():
            if weight > 0 and hero in pool:
                all.append((hero, weight))
        all.sort(key=lambda tup: tup[1])
        return all

    def buildWeighting(self, gradient, heroes):
        self.weighting = {}
        for hero in heroes:
            self.weighting[hero] = 0

        for hero in self.other_characters:
            self.weighting[hero] = gradient

        for i in range(len(self.priority_list)):
            l = self.priority_list[i]
            if l is not None:
                for hero in l:
                    self.weighting[hero] = 1 - (i * gradient)

@auto_str
class Hero:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
