import numpy as np
from cfile_methods import *
import os
class commands():
    def __init__(self): 
        self.commands = []

    def __getitem__(self,idx):
        return self.commands[idx]
    def __len__(self):
        return len(self.commands)
    def __iter__(self):
        for c in commands:
            yield c
    def __str__(self):
        return self.commands

    def info(self, author = None):
        self.commands.append(setInfo(author))
    
    def openFile(self,filename = 'dsplot',cwd = os.getcwd()):
        self.commands.append(setOpenFile(filename,cwd))

    def incl_pythonScript(self,file = ''):
        pass
    def python_cmd(self,cmd = None,*args,**kwargs):
        pass

    def viewpoint(self,view = 'top'):
        self.commands.append(viewpoint(view))

    def zoom(self):
        pass

    def rotate(self,angle,axis = 'X'):
        self.commands.append(rotate(angle,axis))
    
    def screenshot(self,imgName = 'image.png',cwd = os.getcwd(),window = 'OGL1x', gamma = 1.24 ,invert = 0.9,overwrite = False):
        self.commands.append(screenshot(imgName,cwd,window,gamma,invert, overwrite))
    
    