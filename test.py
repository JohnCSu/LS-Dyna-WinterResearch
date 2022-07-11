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

#See contour.py
cmd.plotContour('von-mises')

#See file_io 
cmd.movie(mov_name= 'hello_world')


cmd.plotContour('x-stress')
#See file_io 
cmd.movie(mov_name= 'hello_world2')


#No need to add .cfileextension
cfile.writeTo('hello_world')