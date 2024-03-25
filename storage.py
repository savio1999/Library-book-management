import json
def save_data(file_name,dictionary):
    '''
    Saves existing data to a file 

    Parameters:
            file_name (str): name of the file
            dictionary (dict): dictionary to be saved
    '''
    json_object = json.dumps(dictionary, indent=4)

    with open(file_name, "w") as outfile:
        outfile.write(json_object)
    
    outfile.close() 


def retrive_data(file_name):
    '''
    loads saved database. 
    '''
    with open(file_name, 'r') as openfile:

        json_object = json.load(openfile)

    openfile.close()
    return json_object


