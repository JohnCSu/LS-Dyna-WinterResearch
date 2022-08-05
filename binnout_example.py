import py_dyna as pd


'''
This Example Script shows how to use binnout methods
'''

#basic setup
cfile = pd.cfileOBJ()
cmd = cfile.commands

#Add info at top and file to open
cmd.set_info(author = 'John Su')
cmd.openFile('d3plot')

#Load and set the block of interest
cmd.load_Binout(file='binout0000')
cmd.block_Binout(block = 'dbfsi')


cmd.plotXY_Binout(branches = [1,2],toPlot= 'mout')
cmd.operations_Binout(operations=['differentiate','sum_curves'])
cmd.saveXY(filename='massFlowRate.csv',cwd='')

#Equivalent
cmd.getBinoutPlot(branches= [1,2] , toPlot = 'mout',operations=['differentiate','sum_curves'],filename= 'massFlowRate',saveImg=True)

cfile.writeTo('binout_example')