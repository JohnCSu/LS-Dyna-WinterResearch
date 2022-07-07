import py_dyna as pd

#basic setup
cfile = pd.cfileOBJ()
cmd = cfile.commands


#Add info at top and file to open
cmd.set_info(author = 'John Su')
cmd.openFile('d3plot')


#Set viewpoint
cmd.viewpoint('isometric x')

#Movie 
cmd.movie(mov_name= 'hello_world')

print(cmd)
#No need to add .cfileextension
cfile.writeTo('hello_world')