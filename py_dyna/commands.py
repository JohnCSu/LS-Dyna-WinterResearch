import numpy as np
import os


#THIS IS SUPER HACKY
func_before = dir()
from .methods.file_io import *
from .methods.view import *
from .methods.contour import *
func_after = dir()
imported_funcs = [f for f in func_after if not f in func_before]


from functools import wraps
class commands():
    '''
    Commands Object:

    Essentially a list with a bunch of string methods that will append to the list that will form the command file.

    For clarity, The DocString
    
    
    '''
    def __init__(self,cwd = os.getcwd()): 
        self.commands = []
        
        #Initialise state variables
        self.author = None
        self.timeCreated = None
        self.cwd = cwd
        self.set_DocString()
        self.m = movie


    def __getitem__(self,idx):
        return self.commands[idx]
    def __len__(self):
        return len(self.commands)
    def __iter__(self):
        for c in self.commands:
            yield c
    def __str__(self):
        return ''.join( [c+'\n' for c in self.commands])
            

    def set_DocString(self):
        '''
        Set the Docstring for each method in commands. All documentation is in the methods file to avoid
        This is an unbelievably hacky way of setting the docstrings.
        '''

        for f in imported_funcs:
            if hasattr(self,f):
                x = getattr(self,f)
                y =getattr(x,'__func__')
                y.__doc__ = getattr(globals()[f],'__doc__')

    def set_info(self, author = None):
        if author:
            self.author = author
        self.commands.append(set_info(author))
    
    def openFile(self,filename = 'd3plot'):
        self.commands.append(OpenFile(filename,self.cwd))

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
    
    def screenshot(self,imgName = 'image.png',window = 'OGL1x', gamma = 1.24 ,invert = 0.9,overwrite = False):
        self.commands.append(screenshot(imgName,self.cwd,window,gamma,invert, overwrite))
    
    def movie(self,mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0):
        self.commands.append( movie(mov_name,format,resolution,gamma,FPS,self.cwd) )
    
    
    def state(self,state_no,increment = False):
        self.commands.append( state(state_no,increment))
    

    def plotContour(self,contour = 'von-mises'):
        self.commands.append(plotContour(contour))


if __name__ == '__main__':
    cmd = commands()
    help(cmd.movie)
    # print(dir())