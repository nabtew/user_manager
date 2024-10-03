"""
This module manages the main UI for tool.

It loads data from a JSON file, displays it in a QListwidget, 
and allows the user to add or remove values from the lists.

Dependencies:
    - PyQt5
    - shiboken2
    - user_manager_utils (utility file for handling JSON data)
"""

from PyQt5 import QtWidgets 
import logging
import sys
import os
import ui as user_manage_ui
import importlib
import user_manager_utils as manage_utils

importlib.reload(user_manage_ui)
importlib.reload(manage_utils)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

moduleDir = os.path.dirname(sys.modules[__name__].__file__)
json_data_path = "%s\\Json_user.json" %moduleDir

class user_manage_uir(QtWidgets.QMainWindow):
    """
    user_manage_uir is the main class for manage the UI from 'ui.py' and variable.

    It provides functionality to:
    - Load user data from a JSON file
    - Display keys and values in QListWidgets
    - Add or delete the valuse

    Method:
    display_keys():
        Display the keys on QListWidgets from JFON file.
    display_values():
        Display the values on QListWidgets with selected key.

    """

    def __init__(self, *args, **kwargs):

        # setup the window
        super(user_manage_uir, self).__init__(*args, **kwargs)

        # read the ui
        self.ui = user_manage_ui.Ui_User_manager()
        self.ui.setupUi(self)
        
        self.data_json = manage_utils.read_json(json_data_path) # load data from .json file
        self.data_key = manage_utils.keys_data(self.data_json) # Keys from Dic
        self.data_values = manage_utils.values_data(self.data_json) # Values from Dic

        # Display keys and values in QlistWidget
        self.display_keys()
        self.ui.listName_box.itemClicked.connect(self.display_values)
        # add the value by user
        self.ui.add_button.clicked.connect(self.user_add_value)
        self.ui.delete_button.clicked.connect(self.user_del_volume)
        
   
    def display_keys(self):# list name of the keys from .json show on QlistWidget
        for key in self.data_key:
            self.ui.listName_box.addItem("{}".format(key))

    def display_values(self):#

        if self.ui.listName_box.currentRow() != -1:
            selected_key = self.ui.listName_box.currentItem().text()
            self.ui.listAssets_box.clear()
            self.ui.listAssets_box.addItems(self.data_json[selected_key])

        else:
            self.ui.listAssets_box.clear()

    def user_add_value(self):
        current_item = self.ui.listName_box.currentItem().text()
        value_name_text = self.ui.addName_box.text()
        list_of_data_values = [item for sublist in self.data_values for item in sublist]
        check_value_exists = False

        if value_name_text != "":
            for value in list_of_data_values:
                if value == value_name_text:
                    check_value_exists = True
                    break
                
            if check_value_exists == True:
                logger.error("text name already exists, pls type a new ones")
                
            else:
                self.ui.listAssets_box.addItem(value_name_text)
                manage_utils.write_json(json_data_path, current_item, self.data_json, value_name_text)
                        
        else:
            logger.error("no item to add, pls type any name in the box")
            pass
    
    def user_del_volume(self):
        current_item = self.ui.listName_box.currentItem().text()
        deValume = self.ui.listAssets_box.currentItem().text()
        current_row = self.ui.listAssets_box.currentRow()
        if current_item and deValume:
            self.ui.listAssets_box.takeItem(current_row)
            manage_utils.delete_json(json_data_path, self.data_json, current_item, deValume)
        else:
            logger.error("none value to delete")


"""def run():
    global ui
    try:
        ui.close()
    except:
        pass

    toolUi = user_manage_uir(parent=ptr)
    toolUi.show()"""


def show():
    logger.info('Run in standalone\n')
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    myApp = user_manage_uir()
    myApp.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    show()
