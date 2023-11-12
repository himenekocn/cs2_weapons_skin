from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class SkinsWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Viewer/skins.ui", self)

        self.textToPaste.setText("You console command will be here")
        # self.textToPaste.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textToPaste.setReadOnly(True)
        self.seedLabel.setText(f"{self.seedSlider.value()}")
        self.wearLabel.setText(f"{self.wearSlider.value()}")

        self.seedSlider.valueChanged.connect(self.update_seed)
        self.wearSlider.valueChanged.connect(self.update_wear)

        self.seedSlider.setMinimum(0)
        self.seedSlider.setMaximum(1024)

        self.wearSlider.setMinimum(0)
        self.wearSlider.setMaximum(100000)

    def update_seed(self):
        self.seedLabel.setText(f"{self.seedSlider.value()}")

    def update_wear(self):
        wearValue = self.wearSlider.value() / 100000
        self.wearLabel.setText(f"{wearValue:.5f}")
