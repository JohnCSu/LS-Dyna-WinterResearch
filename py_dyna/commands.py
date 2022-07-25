import numpy as np
import os
from pathlib import PureWindowsPath

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
    def __init__(self,cwd = './'): 
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


    # Functions from file_io.py
    
    def set_info(self, author = None):
        if author:
            self.author = author
        print(locals())
        self.commands.append(set_info(author))
    
    def openFile(self,filename = 'd3plot'):
        self.commands.append(OpenFile(filename,self.cwd))

    def screenshot(self,imgName = 'image.png',window = 'OGL1x', gamma = 1.24 ,invert = 0.9,overwrite = False):
        self.commands.append(screenshot(imgName,self.cwd,window,gamma,invert, overwrite))
    
    def movie(self,mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0):
        self.commands.append( movie(mov_name,format,resolution,gamma,FPS,self.cwd) )
    
    
    def comment(self,text):
        self.commands.append(comment(text))

    # Functions from view.py

    def viewpoint(self,view = 'top'):
        self.commands.append(viewpoint(view))

    def zoom(self):
        pass

    def rotate(self,angle,axis = 'X'):
        self.commands.append(rotate(angle,axis))
    
    def state(self,state_no,increment = False):
        self.commands.append( state(state_no,increment))
    
    # Functions from contour.py

    def plotContour(self,contour, name = None,plot = 'fringe'):
        self.commands.append(plotContour(contour, name = None,plot = 'fringe'))

    def contourRange(self,range,min =None,max = None):
        self.commands.append(contourRange(range,min =None,max = None))



    #Convience Functions

    def ContourMovie(self,mov_name,contour,viewpoint = None,range = 'static',FPS = 10,levels = 10,plot = 'fringe',format = 'MP4/H264'):
        '''
        Convience Function to record movie. For complicated views outside of the default viewpoints (top,bottom,left etc), set the desired view outside of this function
        Inputs:
            mov_name : (str):                   Name of movie file with no ext
            contour: (str or int):              type of contour to display (e.g. von-mises)
            range: str of(tuple) Default 'static': set Contour Range. if static or dynamic can be a single string otherwise add a tuple:
                                                    ('userdef',min , max),First element in tuple is the range type followed by the min val and max val if applicable

            viewpoint: (str) Default: None :    Viewpoint to record. If None uses current viewport
            FPS: (int) Default: 10 :            Number of frames per second
            levels: (int) : Default : 10        Number of Contour Levels
            format: (str) Default: MP4/H264     Format to record  image. MP4 is defult video format set to MJPEG to screenshot every state

        '''
        
        self.comment('Recording Contour Movie')

        if viewpoint is not None:
            self.viewpoint(viewpoint)
    
        self.plotContour(contour=contour,plot=plot)

        if isinstance(str,range):
            self.contourRange(range=range,level = levels)
        else: #Is a tuple which will need to be unpacked
            self.contourRange(*range,level = levels)
        
        self.movie(mov_name = mov_name,FPS = FPS,format=format)

    def ContourPhoto(self,imgName,contour,state,viewpoint = None,range = 'static',levels = 10,plot = 'fringe'):
        '''
        Convience Function to screenshot photo. For complicated views outside of the default viewpoints (top,bottom,left etc), configure that first outside of this function

        Inputs:
            Imgname : (str):                   Name of movie file with extension. Recommended: .png, .jpg
            contour: (str or int):             type of contour to display (e.g. von-mises)
            state: (int)                       The state to take the screenshot in.
            
            range: str of(tuple) Default 'static': set Contour Range. if static or dynamic can be a single string otherwise add a tuple:
                                                    ('userdef',min , max),First element in tuple is the range type followed by the min val and max val if applicable            
            viewpoint: (str) Default: None :    Viewpoint to record. If None uses current viewport
            levels: (int) : Default : 10        Number of Contour Levels
            format: (str) Default: MP4/H264     Format to record  image. MP4 is defult video format set to MJPEG to screenshot every state

        '''

        self.comment('Screenshotting contour photo')
        if viewpoint is not None:
            self.viewpoint(viewpoint)
        #Set State you want to sceenshot

        self.state(state_no=state)

        self.plotContour(contour=contour,plot=plot)
        
        if isinstance(str,range):
            self.contourRange(range=range,level = levels)
        else: #Is a tuple which will need to be unpacked
            self.contourRange(*range,level = levels)
        
        self.screenshot(imgName= imgName)

    
if __name__ == '__main__':
    cmd = commands()
    help(cmd.movie)
    def test(x,y,z):
        print(locals())

    test(x=1,y=2,z=3)