import py_dyna as pd


'''
NOTE as of now, it is assummed that the d3plot file is in the same directory as this script. This allows the cmd file to be
run on both Windows and Linux without worrying with path name sperators. This hopefully will be fixed in the future.


You can find documentation of options in the methods folder (./py_dyna/methods...)

e.g the valid strinfs for plotContour can be found in ./py_dyna/methods/contour.py under plotContour

Use help(cmd.<function>) to print out documentation (some are empty)

Future:
Refactor command code to organise functions into differnet modules so easier to identify

'''

#basic setup
cfile = pd.cfileOBJ()
cmd = cfile.commands


#Add info at top and file to open
cmd.set_info(author = 'John Su')
cmd.openFile('d3plot')

#See view.py
cmd.viewpoint('isometric x')
#Set contour to Static range
cmd.contourRange(crange='static')
#See contour.py
cmd.plotContour('von-mises')
#See file_io 
cmd.movie(mov_name= 'hello_world')

#The above commands can be wrapped together in this single function:
cmd.ContourMovie(mov_name= 'hello_world2',contour='x-displacement',viewpoint= 'isometric y')

#Reset to Default View
cmd.resetView()

#Import a macro that will rotate the model and add to commands
cfile.import_file('rotate.cfile',addToCommands=True)

#Or for debugging we can import the cfile as a list of strings by setting addToCommands to True
# imported_file =cfile.import_file('rotate.cfile',addToCommands=False)
# print(imported_file)


#Take a Photo at state/frame 5. Excluding Viewpoint will take a picture of the current view
cmd.ContourPhoto(imgName='macro.png',contour = 'von-mises',state = 5)

#Generate a global Energy vs time csv file and also generate an image by setting image to True
cmd.historyGlobal(toPlot='Kinetic Energy',filename='global_KE.csv',image = True)

#Add a comment if you want. cfile comments have the prefix $#. The comment function will automatically include one
cmd.comment('Hello World')
cmd.commands.append('closewin')
#No need to add .cfile extension
cfile.writeTo('hello_world')
