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

def write_json(json_data_path, current_item, data_json, value_name_text):
    if current_item in data_json:
        if value_name_text:
            data_json[current_item].append(value_name_text)

        else:
            return
    else:
        return

    with open(json_data_path, "w", encoding="utf-8") as json_file: # open .json 
        json.dump(data_json, json_file, ensure_ascii=False, indent=4)

def delete_json(json_data_path, data_json, current_item, deValume):
    if current_item in data_json:
        data_json[current_item].remove(deValume)

    else:
        data_json[current_item] = [deValume]

    with open(json_data_path, "w", encoding="utf-8") as json_file: # open .json 
        json.dump(data_json, json_file, ensure_ascii=False, indent=4)
   

"""
def write_json(): # A = ชื่อที่ user addเข้ามา, B = listwidget, C = ชื่อที่ user ต้องการลบ
    pass

    add_dic = Dic_json["{}"].format(A) = "{}".format(B) # เพิ่มข้อมูลลง Dictionaries
    del_dic = Dic_json.pop("{}".formate(C))


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = list(car.keys())
print(x[0])
"""