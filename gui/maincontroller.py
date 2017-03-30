import logging
import traceback

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from compositionbuilder import calculateIdealComposition
from gui import mainwindow
from gui.mainmodel import MainModel


class MainController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.model = MainModel(self)

        self.form = mainwindow.Ui_MainWindow()
        self.form.setupUi(self)

        self.composition_comboboxes = [
            self.form.compositionComboBox1,
            self.form.compositionComboBox2,
            self.form.compositionComboBox3,
            self.form.compositionComboBox4,
            self.form.compositionComboBox5,
            self.form.compositionComboBox6
        ]
        self.lineup_comboboxes = [
            self.form.lineupComboBox1,
            self.form.lineupComboBox2,
            self.form.lineupComboBox3,
            self.form.lineupComboBox4,
            self.form.lineupComboBox5,
            self.form.lineupComboBox6
        ]
        # self.picks_graphicsviews = [
        #     self.form.picksGraphicsView1,
        #     self.form.picksGraphicsView2,
        #     self.form.picksGraphicsView3,
        #     self.form.picksGraphicsView4,
        #     self.form.picksGraphicsView5,
        #     self.form.picksGraphicsView6
        # ]
        self.picks_player_labels = [
            self.form.picksPlayerLabel1,
            self.form.picksPlayerLabel2,
            self.form.picksPlayerLabel3,
            self.form.picksPlayerLabel4,
            self.form.picksPlayerLabel5,
            self.form.picksPlayerLabel6
        ]
        self.picks_hero_labels = [
            self.form.picksHeroLabel1,
            self.form.picksHeroLabel2,
            self.form.picksHeroLabel3,
            self.form.picksHeroLabel4,
            self.form.picksHeroLabel5,
            self.form.picksHeroLabel6
        ]

        for i in range(0, 6):
            self.composition_comboboxes[i].setModel(self.model.composition_models[i])
            self.composition_comboboxes[i].currentIndexChanged[str].connect(self.index_changed)

            self.lineup_comboboxes[i].setModel(self.model.lineup_models[i])
            self.lineup_comboboxes[i].currentIndexChanged[str].connect(self.index_changed)

        self.form.runButton.clicked.connect(self.on_run)

        self.form.heroPreferenceTable.setModel(self.model.hero_preference_tm)

        self.open("Overwatch Cup - Hero Preferences.csv")

    def open(self, filename):
        self.model.open(filename)
        self.update_selection()

    @QtCore.pyqtSlot(str)
    def index_changed(self, index):
        self.on_run()

    def on_run(self):
        lineup = self.get_lineup()
        composition = self.get_composition()

        try:
            picks = calculateIdealComposition(lineup, composition)

            i = 0
            for player, hero in picks:
                self.picks_hero_labels[i].setText(hero.name)
                self.picks_player_labels[i].setText(player.battletag)
                i += 1

        except:
            logging.error(traceback.format_exc())

    def update_selection(self):
        cnt = 0
        for lineup_combobox in self.lineup_comboboxes:
            lineup_combobox.setCurrentIndex(cnt)
            cnt += 1
        cnt = 0
        for composition_combobox in self.composition_comboboxes:
            composition_combobox.setCurrentIndex(cnt)
            cnt += 1

    def get_lineup(self):
        lineup = []
        for lineup_combobox in self.lineup_comboboxes:
            lineup.append(self.model.players[lineup_combobox.currentIndex()])
        return lineup

    def get_composition(self):
        composition = []
        for composition_combobox in self.composition_comboboxes:
            composition.append(self.model.heroes[composition_combobox.currentIndex()])
        return composition
