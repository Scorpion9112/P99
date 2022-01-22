import os
import shutil
from stat import *

path=input("Enter the name of the Folder to be checked: ")
days=time.time()

if os.path.exists(path):
    os.walk(path)
    os.path.join(path)
    ctime=os.stat(path).st_ctime
    if ctime>days:
        os.remove(path)
    else:
        shutil.rmtree(path)
        print("Not Found")