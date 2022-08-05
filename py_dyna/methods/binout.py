'''Methods for extracting binout data'''

import os



class binout():
    def __init__(self,file = 'binout',cwd = ''):
        self.file_path = os.path.join(cwd,file)
        self.loadBinout(file,cwd)
    
    def loadBinout(self,file,cwd):
        self.init = 'binaski init'
        self.load = f'binaski load "{self.file_path}"'
        self.fileswitch = f'binaski fileswitch "{self.file_path}"'
        self.start = f'{self.init}\n{self.load}\n{self.fileswitch}'


    def loadBlock(self,block ='dbfsi'):
        self.blockname = block
        self.block = f'binaski loadblock /{block}'
        return self.block

    def plotXY(self,branches,toPlot):
        '''
        branches :int or list/tuple like
        toPlot : str binout dat to plot
        '''
        self.plot = f'binaski plot "{self.file_path}" {self.blockname}'
        print(self.plot)
        if isinstance(branches,int):
        #If only an integer is passed in
            length = 1
            self.plot = f'{self.plot} 1 1 {branches} {toPlot} ;'
        
        
        elif isinstance(branches,list) or isinstance(branches,tuple):
        #If a list or tuple of branches added
            length = len(branches)
            b = ''.join([f'{branch} ' for branch in branches])
            self.plot = self.plot + f' {length} 1 {b}{toPlot} ;'
        return self.plot


    def operations(self,operation):
        '''
        operation: type (str): types of operations to perform on data
        Examples:
            differentiate 
            sum_curves 
        
        '''
        return f'xyplot 1 operation {operation} all'
    


'''
binaski plot "F:\solved\binout0000" dbfsi 2 1 1 2 mout ;

____ {fileloc} {block} {# of branches} {# of Variables to plot} {branch 1} {branch 2} ...

'''