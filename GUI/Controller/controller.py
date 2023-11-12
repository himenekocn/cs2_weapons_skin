from Model.model import Skins
from Viewer.skins import SkinsWidget


class Controller:
    def __init__(self):
        super().__init__()
        self.skins = Skins()
        self.skinswidget = SkinsWidget()

        self.weaponBox = self.skinswidget.weaponBox
        self.skinBox = self.skinswidget.skinBox

        self.skins_details = self.skins.skins_details
        self.weapons = list(self.skins_details.keys())

        self.weaponBox.addItems(self.weapons)
        self.weaponBox.currentIndexChanged.connect(self.update_skins)
        self.skinBox.currentIndexChanged.connect(self.update_skin_id)
        self.skinswidget.generateSkin.clicked.connect(self.generate_skin)

        self.selected_weapon_id = None
        self.selected_skin_id = None

    def update_skins(self):
        selected_weapon = self.weaponBox.currentText()
        self.selected_weapon_id = self.skins.get_weapon_id(selected_weapon)

        if selected_weapon in self.skins_details:
            skins = self.skins_details[selected_weapon]["skins"]
            self.skinBox.clear()
            for skin in skins:
                selected_skin = self.skins.get_skin_name(skin)
                self.skinBox.addItem(selected_skin)

    def update_skin_id(self):
        selected_skin = self.skinBox.currentText()
        self.selected_skin_id = self.skins.get_skin_id(selected_skin)
        return self.selected_skin_id

    def generate_skin(self):
        selected_seed = self.skinswidget.seedSlider.value()
        selected_wear = self.skinswidget.wearSlider.value() / 100000
        selected_weapon = self.selected_weapon_id
        selected_skin = self.selected_skin_id
        self.skinswidget.textToPaste.setText(
            f"skin {selected_skin} {selected_seed} {selected_wear:.5f} {selected_weapon}"
        )
