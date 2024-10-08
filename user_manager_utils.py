import os
import sys 
import json

moduleDir = os.path.dirname(sys.modules[__name__].__file__)

def read_json(json_data_path):
    with open(json_data_path, "r") as json_file:
        data = json.load(json_file)
    return data

def update_key_json(json_data_path, current_item, data_json, value_name_text):
    if current_item in data_json:
        if value_name_text:
            data_json[current_item].append(value_name_text)

        else:
            return
    else:
        return

    with open(json_data_path, "w", encoding="utf-8") as json_file: # open .json 
        json.dump(data_json, json_file, ensure_ascii=False, indent=4)

def delete_value_json(json_data_path, data_json, current_item, delete_value):
    if current_item in data_json:
        data_json[current_item].remove(delete_value)

    else:
        data_json[current_item] = [delete_value]

    with open(json_data_path, "w", encoding="utf-8") as json_file: # open .json 
        json.dump(data_json, json_file, ensure_ascii=False, indent=4)

def show_all(data_json):
    keys_with_none_values = [key for key, value in data_json.items() if value == []]
    return keys_with_none_values
    # return [] or ["Mint","b"]

def check_display_name(listName_box):
    name_count = listName_box.count()
    names = []

    for i in range(name_count):
        name = listName_box.item(i) #get name from position count in QListWidget
        name_text = name.text()
        names.append(name_text)

    return names
