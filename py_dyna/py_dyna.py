import os
# from cfile_methods import cfileMethods
from .commands import commands

#Assume that the script always run in same directory as batch execution 

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


    def writeTo(self,cfile_name =None,mode = 'w'):
        '''
        Inputs:
        new_name : type(str) cfile name to replace current stored name. 
        if None then name is self.name (typically just py_lspost)

        mode: type(str) how to open file. Default is 'w' can also be 'a'
        '''
        #Function writes out the cfile 
        #If a new name is chosen, overide
        if cfile_name:
            self.name = cfile_name.replace('.cfile','')
        
        with open(f'{self.name}.cfile',mode) as f:
            for c in self.commands:
                f.write(c+'\n')
        print(f'{self.name}.cfile has been created!')
    

    #Function independent of instance so can be called whenever
    #Converts a .cfile file into a list of commands
    
    def importcfile(self,file,removeOpen = True, addToCommands = True):
        #Function must contain the .cfile file extension else error is raised
         
        with open(file, 'r') as f:
            #Get rid of 
            cfile = [line.replace('\n','') for line in f.readlines()]
        for cmd in cfile:
            if 'open d3plot' in cmd and removeOpen:
                cfile.remove(cmd)
        
        cfile.insert(0,f'#$ Imported cfile commands from {file} '+ '#'*20 + '\n')

        #Give people the choice to directly append cfile to current commands
        if addToCommands:
            self.commands.add_Cfile(cfile)
            return None
        else:
            return cfile


if __name__ == '__main__':
    cfile = cfileOBJ()
    print(cfile)

    imported_cfile = cfile.importcfile('hello_world.cfile',addToCommands=False)
    print(imported_cfile)

    exit()
    cmd = cfile.commands

    cmd.set_info('John Su')
    cmd.openFile()
    cmd.screenshot()
    cmd.movie()

    cfile.writeTo()
    