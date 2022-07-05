import numpy as np
from cfile_methods import *
import os


def add_to_list(func):
        print('hi')
        def wrapper(*args,**kwargs):
            print(kwargs)
            # self.commands.append(func(**kwargs))
            print(func(**kwargs))
            # func(*args,**kwargs)
        return wrapper

class commands():
    def __init__(self,cwd = os.getcwd()): 
        self.commands = []

        #Initialise state variables
        self.author = None
        self.timeCreated = None
        self.cwd = cwd


    def __getitem__(self,idx):
        return self.commands[idx]
    def __len__(self):
        return len(self.commands)
    def __iter__(self):
        for c in self.commands:
            yield c
    def __str__(self):
        return ''.join( [c+'\n' for c in self.commands])
            

    

    def set_info(self, author = None):
        if author:
            self.author = author
        self.commands.append(setInfo(author))
    
    def openFile(self,filename = 'd3plot'):
        self.commands.append(setOpenFile(filename,self.cwd))

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
    
    # def movie(self,mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0):
    #     self.commands.append(movie(mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0, cwd = os.getcwd()))
    @add_to_list
    def movie(mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0,cwd = os.getcwd):
        return movie(mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0,cwd = os.getcwd)


if __name__ == '__main__':
    cmd = commands()
    print(cmd.movie())