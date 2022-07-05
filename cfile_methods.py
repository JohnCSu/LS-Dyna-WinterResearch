import os

import pandas as pd
import numpy as np
from datetime import datetime
from glob import glob

'''
Really janky way of seperating methods into different folders by having the cfile object inherit these methods
If there is a better way tell me!

Only Use this with the cfile object!!
This contains all the methods to write to the cfile file.

'''


def setOpenFile(dsplotName,cwd):

    return f'open d3plot "{cwd}{dsplotName}"'

def setInfo(author = None):
    return f'#$ LS-PrePost command file created by {author if author else "University of Sydney"}\n#$ Created on {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}'


def screenshot(imgName,cwd = os.getcwd(),window = 'OGL1x', gamma = 1.24 ,invert = 0.9,overwrite = False):
# print png "C:\Users\ShyGuy\Desktop\M06 - Post-Processing\LS-PrePost_2020R1_EN_WI06\image_004.png" gamma 1.40 invert 0.90 enlisted "OGL1x
    filename ,file_ext = imgName.split('.')
    valid_formats = {'png','jpeg','jpg','bmp','tiff'}
    if file_ext not in valid_formats:
        ValueError(f'Please use a supported file firmat: \n{valid_formats}')

    #Dont overwrite and check if file already exists
    if not overwrite and imgName in os.listdir(cwd):
        imgName = filename+str(len(glob(f'{filename}\b\d{1,2}\b.{file_ext}'))+1)+'.' + file_ext
    return f'print {file_ext} "{cwd}{imgName}" gamma {gamma} invert {invert} enlisted "{window}"'


def viewpoint(view = 'top'):
    valid_views = {'top','bottom','front','back','left','right'} #Need to check
    if view in valid_views:
        return view
    else:
        raise ValueError(f'view give is invalid. Check speslling or please choose a view from the following options: \n{valid_views}')

def zoom(x,y,z):
    pass

def rotate(angle,axis = 'X'):
    axis = axis.lower()
    valid_axis = {'x','y','z'}

    if not (isinstance(angle,float) or isinstance(angle,int)):
        raise ValueError('Enter a number (int or float) for angle')

    if axis not in valid_axis:
        raise ValueError('valid Axis\' are x,y or z')

    return f'r{axis} {angle}'
def setContour(self,val):
    pass
def setCountorOptions(self):
    pass