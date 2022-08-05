# Post Processing commands for LS-Dyna PrePost

The package py-dyna.py allows users to easily create command files via python with a more readable and reproducible design.

It is a simple cfile object with a commands attribute which is essentially a glorified list object. the commands object
a list of commands that will be written to a .cfile so function can easily be added

Instuctions: (see test.py for a examples of function calls)  

import py_dyna

cfile = py_dyna.cfileOBJ()  
cmd = cfile.commands  
cmd.function  

NOTE as of now, it is assummed that the d3plot file is in the same directory as this script. This allows the cmd file to be
run on both Windows and Linux without worrying with path name sperators. This hopefully will be fixed in the future.


You can find documentation of options in the methods folder (./py_dyna/methods...)

e.g the valid strinfs for plotContour can be found in ./py_dyna/methods/contour.py under plotContour

Use help(cmd.function) to print out documentation (some are empty)

Future:  
Refactor command code to organise functions into differnet modules so easier to identify
