import os
import sys 
import json

moduleDir = os.path.dirname(sys.modules[__name__].__file__)

def read_json(json_data_path):
    with open(json_data_path, "r") as json_file:
        data = json.load(json_file)
    return data

def keys_data(data_json):
    keys_list = list(data_json.keys())
    return keys_list

def values_data(data_json):
    values_list = list(data_json.values())
    return values_list

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
   