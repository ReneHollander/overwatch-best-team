from PyQt5.QtCore import QAbstractItemModel
from PyQt5.QtCore import QAbstractListModel
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import Qt

from input import readowcsv


class HeroPreferenceTableModel(QAbstractTableModel):
    def __init__(self, parent, model, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.model = model

    def fromIndex(self, index):
        return self.model.heroes[index.row()], self.model.players[index.column()]

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.model.heroes)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.model.players)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        hero, player = self.fromIndex(index)
        return str(player.weighting[hero])

    def setData(self, index, data, role=Qt.DisplayRole):
        try:
            weight = float(data)
            if weight < 0 or weight > 1:
                return False
            hero, player = self.fromIndex(index)
            player.weighting[hero] = weight
            return True
        except ValueError:
            return False

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.model.players[col].battletag
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self.model.heroes[col].name
        return None


class LineupItemModel(QAbstractListModel):
    def __init__(self, parent, model, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.model = model

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.model.players)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        return self.model.players[index.row()].battletag

class CompositionItemModel(QAbstractListModel):
    def __init__(self, parent, model, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.model = model

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.model.heroes)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        return self.model.heroes[index.row()].name

class MainModel():
    def __init__(self, parent):
        self.hero_preference_tm = HeroPreferenceTableModel(parent, self)

        self.lineup_models = []
        for i in range(0, 6):
            self.lineup_models.append(LineupItemModel(parent, self))
        self.composition_models = []
        for i in range(0, 6):
            self.composition_models.append(CompositionItemModel(parent, self))

        self.heroes = []
        self.players = []

    def beginResetModel(self):
        self.hero_preference_tm.beginResetModel()
        for lineup_model in self.lineup_models:
            lineup_model.beginResetModel()
        for composition_model in self.composition_models:
            composition_model.beginResetModel()


    def endResetModel(self):
        self.hero_preference_tm.endResetModel()
        for lineup_model in self.lineup_models:
            lineup_model.endResetModel()
        for composition_model in self.composition_models:
            composition_model.endResetModel()

    def open(self, filename):
        self.beginResetModel()
        self.heroes, self.players = readowcsv(filename, 1 / 4)
        self.endResetModel()
