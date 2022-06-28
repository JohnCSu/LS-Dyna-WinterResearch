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
class cfileMethods():
    def __init__(self):
        pass
    def setOpenFile(self,dsplotName):
    
        return f'open d3plot "{self.cwd}{dsplotName}"'
    
    def setInfo(self,author):
        if author:
            self.author = author
        
        return f'#$ LS-PrePost command file created by {author if author else "University of Sydney"}\n#$ Created on {self.timeCreated}'


    def screenshot(self,imgName = None,window = 'OGL1x', gamma = 1.24 ,invert = 0.9,overwrite = False):
    # print png "C:\Users\ShyGuy\Desktop\M06 - Post-Processing\LS-PrePost_2020R1_EN_WI06\image_004.png" gamma 1.40 invert 0.90 enlisted "OGL1x
        filename ,file_ext = imgName.split('.')
        #Dont overwrite and check if file already exists
        if not overwrite and imgName in os.listdir(self.cwd):
            imgName = filename+'_'+len(glob(f'{filename}*.{file_ext}'))+'.' + file_ext
        return f'print {file_ext} "{self.cwd}{imgName}" gamma {gamma} invert {invert} enlisted "{window}"'


    def setContour(self,val):
        pass
    def setCountorOptions(self):
        pass