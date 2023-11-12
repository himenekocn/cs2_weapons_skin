from Model.model import Skins
from Viewer.skins import SkinsWidget


class Controller:
    def __init__(self):
        super().__init__()
        skins = Skins()
        self.skinswidget = SkinsWidget()

        self.weaponBox = self.skinswidget.weaponBox
        self.skinBox = self.skinswidget.skinBox

        self.skins_details = skins.skins_details
        self.weapons = list(self.skins_details.keys())

        self.weaponBox.addItems(self.weapons)
        self.weaponBox.currentIndexChanged.connect(self.update_skins)

    def update_skins(self):
        selected_weapon = self.weaponBox.currentText()
        if selected_weapon in self.skins_details:
            skins = self.skins_details[selected_weapon]["skins"]
            self.skinBox.clear()
            self.skinBox.addItems([str(skin) for skin in skins])
