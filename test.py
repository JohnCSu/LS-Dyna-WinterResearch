import py_dyna as pd


'''
You can find documentation of options in the methods folder (./py_dyna/methods...)

'''

def func(x):
    return x

a = []

a.append(func)

print(a[0](1))
#basic setup
cfile = pd.cfileOBJ()
cmd = cfile.commands


print(cfile)

imported_cfile = cfile.importcfile('test.cfile',addToCommands=True)
print(cfile.commands)

exit()
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


# from functools import wraps


# def func(x):
#     '''This is a test function'''
#     return x**2  
# class testOBJ():
#     def __init__(self):
#         self.test = []
#         self.wrap = self.wrapper_function(func)
#         self.wrap(4)
#         print(self.test)

    
#     def wrapper_function(self,func):
#         '''Wraps Each Function to append looks cleaner'''
#         @wraps(func)
#         def inner_function(*args,**kwargs):
#             self.test.append(func(*args,**kwargs))
#         return inner_function

# print(func.__)

# class cwd_Obj():
#     '''
#     Really hacky way to do this. Basically dont execute the string 
#     '''
#     def __init__(self,func,*args,**kwargs):
#         self.func = func
#         self.args = args
#         self.kwargs = kwargs
#     def __call__(self,platform = 'windows'):
#         '''
#         Can be either windows or linux 
#         Delays the calling of a function until at execution
#         '''

#         return self.func(*self.args,**self.kwargs)

# # a = cwd_Obj(func,x=9)


