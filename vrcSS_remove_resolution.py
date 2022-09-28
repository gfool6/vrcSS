import glob
import re
import os
import shutil
import tkinter
import tkinter.filedialog

iDir = os.path.abspath(os.path.dirname(__file__))
folder_name = tkinter.filedialog.askdirectory(initialdir=iDir)

files = [screenShots for screenShots in glob.glob(folder_name+'/VRChat*.png')]
filenameList = [f"{ssfile}" for ssfile in files]

for filename in filenameList:
    print(filename)
    [shutil.move(f"{filename}", f"{re.sub('_[0-9]+x[0-9]+_', '_', filename)}")]
