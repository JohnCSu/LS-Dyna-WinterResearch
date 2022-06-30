import os

import pandas as pd
import numpy as np
from datetime import datetime
from glob import glob
from collections import OrderedDict
# from cfile_methods import cfileMethods
from cfile_methods import cfileMethods
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


#Currently only cfileOBJ
class ls_dyna_OBJ():
    def __init__(self):
        self.cwd = os.getcwd()
        self.cfile = self.set_cfile()

    def set_cfile(self,cfileName = None ):
        if cfileName:
            self.cfileName = cfileName
        else:
            self.cfileName = 'py_lspost'
        return cfileOBJ(self.cfileName,cwd = self.cwd)
        

class cfileOBJ(cfileMethods):
    def __init__(self,cfilename = 'py_lspost',cwd = os.getcwd(),dsplotName = 'dsplot', author = None):
        '''
        Inputs:
        cfilename: Name of cfile. cfile extension if included is removed

        cwd: working directory. By default assumes that the object is created in the same directory as the dsplot

        dsplotName: LS-dyna file to open. By default it will try and open dsplot
        
        author: author's Name
        
        
        '''
        super().__init__()
        #Only Store the filename not file extension. If file extension is added just remove it
        self.name = cfilename.replace('.cfile','')
        self.cwd = cwd+os.sep
        self.dsplotName = dsplotName
        self.author = author
        #Get time of creation
        self.timeCreated = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        #Set comments at top of cfile
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


    def writeCfig(self,new_name =None,new_dsplotName = None,mode = 'w'):
        '''
        Inputs:
        new_name : type(str) cfile name to replace current stored name. Default None

        new_dsplotName: type(str) for dsplot to open. Default: None
        
        mode: type(str) how to open file. Default is 'w' can also be 'a'
        '''
        #Function writes out the cfile 
        #If a new name is chosen, overide
        if new_name:
            self.name = new_name.replace('.cfile','')
        
        if self.dsplotName is None and new_dsplotName is None:
            raise ValueError('A dsplot files needs to be chosen')
        elif new_dsplotName:
            self.dsplotName = new_dsplotName
        
        self.commands['file'] = self.setOpenFile(self.dsplotName)
        
        with open(f'{self.name}.cfile',mode) as f:
            f.write(self.commands['header'] + '\n')
            f.write(self.commands['file'] + '\n')
            for c in self.commands['contents']:
                f.write(c+'\n')
        print(f'{self.name}.cfile has been created!')
    

    #Function independent of instance so can be called whenever
    #Converts a .cfile file into a list of commands
    @staticmethod
    def importcfile(file,removeHeader = True):
        #Function must contain the .cfile file extension else error is raised    
        with open(file, 'r') as f:
            cfile = str.split(f.readlines(),'\n')
        if removeHeader:
            #If removeHeader is true, remove the description as well as the open 3dsplot function.
            #These will always be the first 3 lines
            #Maybe also find open 3dsplot line and slice from there is a more robust way?
            return cfile[3:]
        else:
            return cfile



if __name__ == '__main__':
    lsOBJ = ls_dyna_OBJ()
    cfile = lsOBJ.cfile
    print(cfile)
    cfile.write()
    # commands = cfile.commands
    # print(commands)