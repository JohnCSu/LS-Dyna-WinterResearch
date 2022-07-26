import py_dyna as pd


'''
You can find documentation of options in the methods folder (./py_dyna/methods...)

'''

#basic setup
cfile = pd.cfileOBJ()
cmd = cfile.commands



#Add info at top and file to open
cmd.set_info(author = 'John Su')
cmd.openFile('d3plot')

#Set view.py
cmd.viewpoint('isometric x')
#Set contour Static
cmd.contourRange(crange='static')
#See contour.py
cmd.plotContour('von-mises')
#See file_io 
cmd.movie(mov_name= 'hello_world')


#The above commands can be wrapped together in a single function:
cmd.ContourMovie(mov_name= 'hello_world2',contour='x-displacement',viewpoint= 'isometric y')

#Reset to Default View
cmd.resetView()

#Import a macro that will rotate the cfile
imported_cfile = cfile.import_file('rotate.cfile',addToCommands=True)

#Take a Photo at state 5. Excluding Viewpoint will take a picture of the current view
cmd.ContourPhoto(imgName='macro.png',contour = 'von-mises',state = 5)
#No need to add .cfileextension
cfile.writeTo('hello_world')
