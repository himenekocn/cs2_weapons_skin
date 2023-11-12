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

    def skins_json_to_dict(self):
        with open('Model/skins.json') as json_file:
            self.skins_details = json.load(json_file)
        return self.skins_details

    # def skins_dump_yml_to_dict(self):
    #     with open('Model/skins_dump.yml', encoding='utf-8') as self.skins_dump_yml:  # Specify the encoding
    #         try:
    #             # Load YAML string into Python objects
    #             self.skins_dump_obj = yaml.safe_load(self.skins_dump_yml)

    #             # Convert Python objects to JSON string
    #             self.skins_dump_json = json.dumps(self.skins_dump_obj, indent=2)

    #             self.skins_dump_dict = json.loads(self.skins_dump_json)  # Use json.loads, not json.load

    #             print(self.skins_dump_dict)

    #         except Exception as e:
    #             print(f"Error converting YAML to JSON: {str(e)}")

    #     return self.skins_dump_dict


    
# skin number template wear

