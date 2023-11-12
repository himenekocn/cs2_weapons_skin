from PyQt5.QtWidgets import QApplication
from Viewer.skins import SkinsWidget
from Controller.controller import Controller
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    mainwindow = controller.skinswidget
    mainwindow.setWindowTitle("OSTORA Skins")
    mainwindow.show()
    app.exec_()
