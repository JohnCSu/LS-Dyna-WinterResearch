from warnings import warn
import os
def historyGlobal(toPlot):
    '''
    Command to plot global XY value against time. 
    
    toPlot: str or int 
    
    if str it will check it with the Global_dict and match the string to the corresponding integer.
    Alternatively you can directly pass an integer in although ensuring it is the correct integer is up
    to the user

    '''
    Global_dict = {
        'Kinetic Energy':1,
        'Internal Energy':2,
        'Total Energy':3,
        
        'X-Rigid Displacement':4,
        'Y-Rigid Displacement':5,
        'Z-Rigid Displacement':6,
        'Resultant-Rigid Displacement':7,

        'X-Rigid Velocity':8,
        'Y-Rigid Velocity':9,
        'Z-Rigid Velocity':10,
        'Resultant-Rigid Velocity':11,


        'X-Rigid Acceleration':12,
        'Y-Rigid Acceleration':13,
        'Z-Rigid Acceleration':14,
        'Resultant-Rigid Acceleration':15,
        'Rigid Wall Force, wall#1':16
    }
    if isinstance(toPlot,str):
        value = Global_dict[toPlot]
        return f'gtime {value}'
    elif isinstance(toPlot,int):
        warn('Integer for name please check that the integer is a valid key')
        return f'gtime {toPlot}'
    else:
        raise ValueError('Function only excepts type str or int')



def historyNodal(nodes,toPlot):
    '''
    Command to plot Nodal XY value against time. 
    
    nodes: iterable (e.g list or tuple) of node ids that will be plotted e.g [1,4,2] will plot nodes 1, 4 and 2. order does not matter
    
    toPlot: str or int 
    if str it will check it with the Nodal_dict and match the string to the corresponding integer.
    Alternatively you can directly pass an integer in although ensuring it is the correct integer is up
    to the user


    '''
    Nodal_dict = {
        'X-coordinate': 1,
        'Y-coordinate': 2,
        'Z-coordinate': 3,
        'Total-coordinate': 4,

        'X-Displacement':5,
        'Y-Displacement':6,
        'Z-Displacement':7,
        'Resultant-Displacement':8,

        'X-Velocity':9,
        'Y-Velocity':10,
        'Z-Velocity':11,
        'Resultant-Velocity':12,


        'X-Acceleration':13,
        'Y-Acceleration':14,
        'Z-Acceleration':15,
        'Resultant-Acceleration':16,

    }
    plot = ''
    #Assume only one part for now...
    for node in nodes:
        plot += 'genselect node add node {node}/0\n'


    if isinstance(toPlot,str):
        value = Nodal_dict[toPlot]
        plot += 'ntime {value}\n'
    elif isinstance(toPlot,int):
        warn('Integer for name please ensure that the given integer is a valid key')
        plot += 'ntime {value}\n'
    else:
        raise ValueError('Function only excepts type str or int')
    
    plot += 'clearpick'

    return plot


def XYtoCSV(filename,cwd):
    path = os.path.join(cwd,filename)
    return f'xyplot 1 savefile ms_csv "{path}" 1 all'