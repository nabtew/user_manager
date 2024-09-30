import os
import sys 
import json

moduleDir = os.path.dirname(sys.modules[__name__].__file__)

def load_json(json_data_path):
    with open(json_data_path, "r") as Jfile:
        data = json.load(Jfile)
    return data

def name_data(data):
    data_list = list(data.keys())
    return data_list

def list_widget(data):
    widget_list = list(data.values())
    
    return widget_list

def writeJson(json_data_path, crItem, mut, valueName):
    if crItem in mut:
        if valueName:
            mut[crItem].append(valueName)

        else:
            return
    else:
        return

    with open(json_data_path, "w", encoding="utf-8") as json_file: # open .json 
        json.dump(mut, json_file, ensure_ascii=False, indent=4)

def delJson(json_data_path, mut, crItem, deValume):
    if crItem in mut:
        mut[crItem].remove(deValume)

    else:
        mut[crItem] = [deValume]

    with open(json_data_path, "w", encoding="utf-8") as json_file: # open .json 
        json.dump(mut, json_file, ensure_ascii=False, indent=4)
   

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