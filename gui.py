import sys

from PyQt5.QtWidgets import QApplication

from gui.maincontroller import MainController

app = QApplication(sys.argv)
c = MainController()
c.show()
sys.exit(app.exec_())
