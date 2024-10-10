from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
import logging
import sys
import os
import ui as manage_ui
import importlib
import user_manager_utils as utils

importlib.reload(manage_ui)
importlib.reload(utils)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

moduleDir = os.path.dirname(sys.modules[__name__].__file__)
json_data_path = "%s\\Json_user.json" %moduleDir

class UserManagerUi(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):

        # setup the window
        super(UserManagerUi, self).__init__(*args, **kwargs)

        # read the ui
        self.ui = manage_ui.Ui_User_manager()
        self.ui.setupUi(self)
        self.data_json = utils.read_json(json_data_path) # load data from .json file

        # Display keys and values in QlistWidget
        self.display_keys()
        self.ui_connect()
        self.visible_key()
        self.ui.checkBox.clicked.connect(self.check_box)

    def ui_connect(self):
        self.ui.listName_box.itemClicked.connect(self.display_values)
        # add the value by user
        self.ui.add_button.clicked.connect(self.user_add_value)
        self.ui.delete_button.clicked.connect(self.user_del_volume)
        self.ui.search_button.clicked.connect(self.search_key)

    def check_box(self):
        check_bool = self.ui.checkBox.isChecked()
        if check_bool:
            self.ui.listName_box.clear()
            self.ui.listAssets_box.clear()
            self.display_keys()

        else:
            self.ui.listName_box.clear()
            self.ui.listAssets_box.clear()
            self.display_keys()
            self.visible_key()

    def display_keys(self):# list name of the keys from .json show on QlistWidget
        for key in self.data_json.keys():
            self.ui.listName_box.addItem("{}".format(key))

    def display_values(self):#

        if self.ui.listName_box.currentRow() != -1:
            selected_key = self.ui.listName_box.currentItem().text()
            self.ui.listAssets_box.clear()
            if self.data_json[selected_key] != None:
                self.ui.listAssets_box.addItems(self.data_json[selected_key])

            else:
                pass

        else:
            self.ui.listAssets_box.clear()

    def user_add_value(self):
        current_item = self.ui.listName_box.currentItem().text()
        value_name_text = self.ui.addName_box.text()
        list_of_data_values = [item for sublist in self.data_json.values() for item in sublist]
        check_value_exists = False

        if value_name_text != "":
            for value in list_of_data_values:
                if value == value_name_text:
                    check_value_exists = True
                    break
                else:
                    check_value_exists = False
                
            if check_value_exists:
                key_found = next((key for key, values in self.data_json.items() if value_name_text in values), None)
                QMessageBox.warning(self, "Warning", f"text name '{value_name_text}' already exists in '{key_found}', please type a new one")
                
            elif check_value_exists == False:
                self.ui.listAssets_box.addItem(value_name_text)
                utils.update_key_json(json_data_path, current_item, self.data_json, value_name_text)
            
        else:
            QMessageBox.warning(self, "Error", "No item to add, please type any name in the box")
            pass
    
    def user_del_volume(self):
        current_item = self.ui.listName_box.currentItem().text()
        delete_value = self.ui.listAssets_box.currentItem()
        if delete_value:
            delete_value = delete_value.text()
        current_row = self.ui.listAssets_box.currentRow()

        if current_item and delete_value:
            self.ui.listAssets_box.takeItem(current_row)
            utils.delete_value_json(json_data_path, self.data_json, current_item, delete_value)

        elif delete_value == None:
            QMessageBox.warning(self, "Error", "none value to delete")
    
    def search_key(self):
        key_name_search = self.ui.search_box.text()
        key_found = utils.find_key(self.data_json, key_name_search)
        if key_name_search == key_found:
            self.ui.listName_box.clearSelection()
            matching_items = self.ui.listName_box.findItems(key_name_search, Qt.MatchExactly)
            if matching_items:
                self.ui.listName_box.setCurrentItem(matching_items[0])
                self.display_values()

            else:
                pass

    def visible_key(self):
        show_all_data = utils.show_all(self.data_json)
        if show_all_data != []:

            for none_value_key in show_all_data:
                matching_items = self.ui.listName_box.findItems(none_value_key, Qt.MatchExactly)
                if matching_items:
                    row = self.ui.listName_box.row(matching_items[0])
                    self.ui.listName_box.takeItem(row)
                else:
                    pass
            
def show():
    logger.info('Run in standalone\n')
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    myApp = UserManagerUi()
    myApp.show()
    sys.exit(app.exec()) #exec_ will be remove in the future, so use "exec()"
    

if __name__ == '__main__':
    show()
