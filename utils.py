import json
from os.path import abspath

class Utils:
    def read_keys()->json: 
        f = open('keys.json')
        data = json.load(f)
        f.close()
        return data

    def read_prompt()->str:
        with open('prompt.txt') as f:
            lines = f.readlines()
        return " ".join(lines)
    
    def save_response(name:str,content:str)->None:
        json_object = json.dumps(content, indent=4)
        with open(f"{name}.json", "w") as outfile:
            outfile.write(json_object)