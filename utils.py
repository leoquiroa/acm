import json

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
    