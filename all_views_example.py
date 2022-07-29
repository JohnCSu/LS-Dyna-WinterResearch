import py_dyna as pd


'''
This Example Script shows how to get an movie of each default view.
This can be useful for monitoring the simulation during runtime
'''

#basic setup
cfile = pd.cfileOBJ()
cmd = cfile.commands

#Add info at top and file to open
cmd.set_info(author = 'John Su')
cmd.openFile('d3plot')

for view in ['top','bottom','left','right','front','back']:
    m_name = f'{view}_view_example'
    cmd.ContourMovie(mov_name= m_name,contour='x-displacement',viewpoint= view)

cfile.writeTo('all_views_example')