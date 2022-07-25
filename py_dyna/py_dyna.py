import os
# from cfile_methods import cfileMethods
from .commands import commands

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


#To do once I learn the Python API for LS-Dyna
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


######################################################## USE ME BELOW ##################################################################

class cfileOBJ():
    def __init__(self,cfilename = 'py_lspost',cwd = '', author = None):
        '''
        Inputs:
        cfilename: Name of cfile. cfile extension if included is removed

        cwd: working directory. By default assumes that the object is created in the same directory as the dsplot

        dsplotName: LS-dyna file to open. By default it will try and open dsplot
        
        author: author's Name
        
        '''
        #Only Store the filename not file extension. If file extension is added just remove it
        self.name = cfilename.replace('.cfile','')
        self.cwd = cwd
        self.author = author
        self.commands = commands(cwd)

    def __str__(self):
        return f''


    def writeTo(self,new_name =None,mode = 'w'):
        '''
        Inputs:
        new_name : type(str) cfile name to replace current stored name. 
        if None then name is self.name (typically just py_lspost)
    
        mode: type(str) how to open file. Default is 'w' can also be 'a'
        '''
        #Function writes out the cfile 
        #If a new name is chosen, overide
        if new_name:
            self.name = new_name.replace('.cfile','')
        
        with open(f'{self.name}.cfile',mode) as f:
            for c in self.commands:
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
    cmd = cfile.commands

    cmd.set_info('John Su')
    cmd.openFile()
    cmd.screenshot()
    cmd.movie()

    cfile.writeTo()
    