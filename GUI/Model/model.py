import json
import yaml


class Skins:
    def __init__(self):
        self.skins_details = None
        self.skins_dump_dict = None
        self.skins_dump_yml = None
        self.skins_dump_json = None
        self.skins_dump_obj = None
        self.skins_json_to_dict()
        self.weapons_id_to_name()
        self.skins_id_to_name()

    def skins_json_to_dict(self):
        with open("Model/skins.json") as json_file:
            self.skins_details = json.load(json_file)
        return self.skins_details

    def weapons_id_to_name(self):
        self.weapon_ids = [
            weapon_data["id"] for weapon_data in self.skins_details.values()
        ]
        return self.weapon_ids

    def get_weapon_id(self, weapon_name):
        return self.skins_details[weapon_name]["id"]

    def get_skin_id(self, skin_name):
        self.reverse_mapping = {
            name: skin_id for skin_id, name in self.skins_dump_obj.items()
        }
        return self.reverse_mapping.get(skin_name, "ID not found")

    def get_skin_name(self, skin_id):
        with open("Model/skins_dump.yml", encoding="utf-8") as self.skins_dump_yml:
            self.skins_dump_obj = yaml.safe_load(self.skins_dump_yml)
        return self.skins_dump_obj.get(skin_id, "Skin not found")

    def skins_id_to_name(self):
        # Get all skins id
        unique_skins_ids = sorted(
            set(
                skin_id
                for weapon_data in self.skins_details.values()
                for skin_id in weapon_data.get("skins", [])
            )
        )
