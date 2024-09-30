from PySide6 import QtWidgets 
from PySide6 import QtCore 
from PySide6 import QtGui
from PySide6 import QtUiTools
import sys
import os
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance
from working import ui as userManage
import importlib
from working import user_manager_utils as manageUtils

importlib.reload(userManage)
importlib.reload(manageUtils)

import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
moduleDir = os.path.dirname(sys.modules[__name__].__file__)
maya_ptr = omui.MQtUtil.mainWindow()
json_data_path = "%s\\Json_user.json" %moduleDir
ptr = wrapInstance(int(maya_ptr), QtWidgets.QWidget)

class UserManager(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        #Setup Window
        super(UserManager, self).__init__(*args, **kwargs)

        # ui read
        self.ui = userManage.Ui_User_manager()
        self.ui.setupUi(self)
        
        self.mut = manageUtils.load_json(json_data_path) # load data from .json
        self.kDic = manageUtils.name_data(self.mut) # Keys from Dic
        self.vDic = manageUtils.list_widget(self.mut) # Values from Dic
        print("keys: ", self.kDic)
        print("value: ", self.vDic)

        # Display keys and values in QlistWidget
        self.write_data()
        self.ui.listName_box.currentItemChanged.connect(self.show_values)
        # add the value by user
        self.ui.add_button.clicked.connect(self.user_addValue)
        self.ui.delete_button.clicked.connect(self.user_delVolume)
   
    def show_values(self):
        selected_key = self.ui.listName_box.currentItem().text()
        self.ui.listAssets_box.clear()
        self.ui.listAssets_box.addItems(self.mut[selected_key])

    def write_data(self):
        for key in self.kDic:
            self.ui.listName_box.addItem("{}".format(key))

    def user_addValue(self):
        crItem = self.ui.listName_box.currentItem().text()
        valueName = self.ui.addName_box.text()
        print(valueName)
        if isinstance(valueName, str):
            self.ui.listAssets_box.addItem(valueName)
            manageUtils.writeJson(json_data_path, crItem, self.mut, valueName)
        else:
            print("has no item to add, pls write any name in the box")
            return
    
    def user_delVolume(self):
        crItem = self.ui.listName_box.currentItem().text()
        deValume = self.ui.listAssets_box.currentItem().text()
        crRow = self.ui.listAssets_box.currentRow()
        print(crRow)
        if crItem and deValume:
            self.ui.listAssets_box.takeItem(crRow)
            manageUtils.delJson(json_data_path, self.mut, crItem, deValume)
        else:
            print("none value to delete")


def run():
    global ui
    try:
        ui.close()
    except:
        pass

    toolUi = UserManager(parent=ptr)
    toolUi.show()


"""def show():
    logger.info('Run in standalone\n')
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    myApp = UserManager()
    myApp.show()
    sys.exit(app.exec_())
    """

"""if __name__ == '__main__':
    run()
"""