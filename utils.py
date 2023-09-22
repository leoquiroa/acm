import json
from datetime import date

class Utils:

    def read_json(file_name:str)->json: 
        f = open(file_name)
        data = json.load(f)
        f.close()
        return data

    def read_prompt_file()->str:
        with open('Configs\\prompt.txt') as f:
            lines = f.readlines()
        return " ".join(lines)
    
    def save_response_as_json(name:str,content:str)->None:
        json_object = json.dumps(content, indent=4)
        with open(f"{name}.json", "w") as outfile:
            outfile.write(json_object)

    def get_today_date():
        today = date.today()
        return today.strftime("%Y-%m-%d")
        