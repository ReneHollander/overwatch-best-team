import logging
import traceback

from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtWidgets import QGraphicsScene
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
        self.player_pick_labels = [
            self.form.playerPickLabel1,
            self.form.playerPickLabel2,
            self.form.playerPickLabel3,
            self.form.playerPickLabel4,
            self.form.playerPickLabel5,
            self.form.playerPickLabel6
        ]
        self.hero_graphicsviews = [
            self.form.heroGraphicsView1,
            self.form.heroGraphicsView2,
            self.form.heroGraphicsView3,
            self.form.heroGraphicsView4,
            self.form.heroGraphicsView5,
            self.form.heroGraphicsView6
        ]

        for i in range(0, 6):
            self.composition_comboboxes[i].setModel(self.model.composition_models[i])
            self.composition_comboboxes[i].currentIndexChanged[str].connect(self.index_changed)

            self.lineup_comboboxes[i].setModel(self.model.lineup_models[i])
            self.lineup_comboboxes[i].currentIndexChanged[str].connect(self.index_changed)
        for gv in self.hero_graphicsviews:
            gv.viewport().installEventFilter(self)

        self.form.heroPreferenceTable.setModel(self.model.hero_preference_tm)

        self.open("Overwatch Cup - Hero Preferences.csv")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            return True
        return False

    def open(self, filename):
        self.model.open(filename)
        self.update_selection()

    @QtCore.pyqtSlot(str)
    def index_changed(self, index):
        composition = self.get_composition()

        for i in range(0, 6):
            hero = composition[i]
            cb = self.composition_comboboxes[i]
            gv = self.hero_graphicsviews[i]

            image = QImage("res/portraits/" + hero.simplename() + ".png")

            scene = QGraphicsScene()
            item = QGraphicsPixmapItem(QPixmap.fromImage(image))
            scene.addItem(item)
            gv.setScene(scene)

        self.run()

    def run(self):
        lineup = self.get_lineup()
        composition = self.get_composition()

        try:
            picks = calculateIdealComposition(lineup, composition)

            i = 0
            for player, hero in picks:
                idx = composition.index(hero)
                composition[idx] = None
                self.player_pick_labels[idx].setText(player.battletag)

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
