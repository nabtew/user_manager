#install command
 
import sys

test_dir = r"D:\nabtew\3d\intern\QT5\file\user_manager"
systemPath = sys.path
if test_dir not in systemPath:
    systemPath.append(test_dir)
    
import app
import importlib
importlib.reload(app)
app.run()