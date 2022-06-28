import os

import pandas as pd
import numpy as np
from datetime import datetime
from glob import glob
from collections import OrderedDict

#Assume that the script always run in same directory as batch execution 
'''
To Do:

- Check current functions are working
- Move them to another script to avoid clutter
- Add:
    -Take snapshot
    -Record Movie
    -Set contour options
- Need to map contour names (e.g. von mises stress) to contour indexing... (sigh)
- This is not going to be just one script to avoid cluttering

Possible Changes:

- Make commands an ordered dict?
    - Header Info
    - Open File
    - Commands
-Check if dsplot is in path


Key Assumptions:
-Header is special
-First dsplot is special should really just assume 
-The script does not check if dsplot exists

'''


#Currently only cfigOBJ
class ls_dyna_OBJ():
    def __init__(self):
        self.cwd = os.getcwd()
        self.cfig = self.set_cfig()

    def set_cfig(self,cfigName = None ):
        if cfigName:
            self.cfigName = cfigName
        else:
            self.cfigName = 'py_lspost'
        return cfigOBJ(self.cfigName,cwd = self.cwd)
        

class cfigOBJ():
    def __init__(self,cfigname = 'py_lspost',cwd = os.getcwd(),dsplotName = 'dsplot', author = None):
        #Only Store the filename not file extension. If file extension is added just remove it
        self.name = cfigname.replace('.cfig','')
        self.cwd = cwd
        self.dsplotName = dsplotName
        self.author = author
        #Get time of creation
        self.timeCreated = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        #Set comments at top of cfig
        self.info = self.setInfo(author )
        #Commands is a list of strings.
        print('hi')
        #Each element corresponds to an action e.g 'rx 10'

        self.commands = OrderedDict()
        self.commands['header'] = self.info
        self.commands['file'] = self.setOpenFile(dsplotName)
        self.commands['contents'] = []

    def __str__(self):
        return self.info


    def write(self,new_name =None,new_dsplotName = None,mode = 'w'):
        '''
        Inputs:
        new_name = string for cfig name
        new_dsplotName: type(str) for dsplot to open
        mode: type(str) how to open file. Default is 'w' can also be 'a'
        '''
        #Function writes out the cfig 
        #If a new name is chosen, overide
        if new_name:
            self.name = new_name.replace('.cfig','')
        
        if self.dsplotName is None and new_dsplotName is None:
            raise ValueError('A dsplot files needs to be chosen')
        elif new_dsplotName:
            self.dsplotName = new_dsplotName
        
        self.commands['file'] = self.setOpenFile(self.dsplotName)
        
        with open(f'{self.name}.cfig',mode) as f:
            f.write(self.commands['header'] + '\n')
            f.write(self.commands['file'] + '\n')
            for c in self.commands['contents']:
                f.write(c+'\n')
        print(f'{self.name}.cfig has been created!')
    

    #Function independent of instance so can be called whenever
    #Converts a .cfig file into a list of commands
    @staticmethod
    def importcfig(file,removeHeader = True):
        #Function must contain the .cfig file extension else error is raised    
        with open(file, 'r') as f:
            cfig = str.split(f.readlines(),'\n')
        if removeHeader:
            #If removeHeader is true, remove the description as well as the open 3dsplot function.
            #These will always be the first 3 lines
            #Maybe also find open 3dsplot line and slice from there is a more robust way?
            return cfig[3:]
        else:
            return cfig
    def setInfo(self,author):
        if author:
            self.author = author
        
        return f'#$ LS-PrePost command file created by {author if author else "University of Sydney"}\n\
        #$ Created on {self.timeCreated}'

    def setOpenFile(self,dsplotName):
        return f'open d3plot "{self.cwd}{os.sep}{dsplotName}"'


if __name__ == '__main__':
    lsOBJ = ls_dyna_OBJ()
    cfig = lsOBJ.cfig
    print(cfig)
    cfig.write()
    # commands = cfig.commands
    # print(commands)