from util import auto_str


@auto_str
class Player:
    def __init__(self, name, battletag):
        self.name = name
        self.battletag = battletag
        self.priority_list = []
        self.other_characters = []

    def __repr__(self):
        return self.__str__()


@auto_str
class Hero:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.__str__()
