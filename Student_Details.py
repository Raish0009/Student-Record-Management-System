import json
def Details(path):
    with open(path,"r") as file:
        data = json.load(file)
        pretty_data = json.dumps(data, indent=4)
        
    return pretty_data