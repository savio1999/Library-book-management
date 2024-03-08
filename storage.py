
import json


def save_data(file_name,dictionary):
    

    json_object = json.dumps(dictionary, indent=4)

    with open(file_name, "w") as outfile:
        outfile.write(json_object)
    
    outfile.close() 


def retrive_data(file_name):
    with open(file_name, 'r') as openfile:

        json_object = json.load(openfile)

    openfile.close()
    return json_object


