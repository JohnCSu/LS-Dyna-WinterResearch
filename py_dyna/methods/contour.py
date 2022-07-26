import warnings

from numpy import isin

def plotContour(contour, name = None,plot = 'fringe'):
    '''
    Plot the contour of the model.

    LS-dyna uses integers to map to field contours. For example,
    x-stress is keyed 1
    y-stress is keyed to 2 etc.

    Inputs
        Contour: type str or int

            String: returns the contour output listed in the dictionary below

            Int: instead of using a string, use the field key directly. This can be
                used to plot contours not listed in the dictionary below


        Name (Optional): Only used if contour is an int
            ignored if contour is a string
            String: gives a name to the new contour

        plot (default = fringe): String argument to set plotting style 
            choices are fringe, 'fringe',isosurf', 'contour''isofringe'}



        The following strings can be used to plot 

        'x-stress': 1,
        'y-stress': 2,
        'z-stress': 3,
        'xy-stress': 4,
        'yz-stress': 5,
        'zx-stress' : 6,
        'effective plastic strain':7,
        'pressure': 8,
        'von-mises':9,

        'signed von-mises':530,

        'x-displacement': 17,
        'y-displacement': 18,
        'z-displacement': 19,
        'resultant displacement':20

    '''

    contour_dic = {
        #Stress Contours
        'x-stress': 1,
        'y-stress': 2,
        'z-stress': 3,
        'xy-stress': 4,
        'yz-stress': 5,
        'zx-stress' : 6,
        'effective plastic strain':7,
        'pressure': 8,
        'von-mises':9,
        '1st-prin dev stress':10,
        '2nd-prin dev stress':11,
        '3rd-prin dev stress':12,
        'tresca':13,
        '1st-principal stress':14,
        '2nd-principal stress':15,
        '3rd-principal stress':16,
        'max in-plane stress': 518,
        'max in-plane stress': 519,
        'signed von-mises':530,


        #Displacement
        'x-displacement': 17,
        'y-displacement': 18,
        'z-displacement': 19,
        'result displacement':20,
        'xy-displacement': 64,
        'yz-displacement': 65,
        'xz-displacement': 66,

        #Velocity
        'x-velocity': 21,
        'y-velocity': 22,
        'z-velocity': 23,
        'result velocity':24,

        #acceleration
        'x-acceleration': 231,
        'y-acceleration': 232,
        'z-acceleration': 233,
        'result acceleration':234,

        #Relative Displacement
        'rx-displacement': 117,
        'ry-displacement': 118,
        'rz-displacement': 119,
        'r-result disp':120,

        #Coordinate
        'x-coordinate':246,
        'y-coordinate':247,
        'z-coordinate':248,

        #Strain
        'x-strain': 601,
        'y-strain': 602,
        'z-strain': 603,
        'xy-strain': 604,
        'yz-strain': 605,
        'zx-strain' : 606,
        'mean strain':608,
        'effective strain': 609,
        '1st-prin. deviatoric':610,
        '2nd-prin. deviatoric':611,
        '3rd-prin. deviatoric':612,
        'max shear strain': 613,
        '1st-principal strain':614,
        '2nd-principal strain':615,
        '3rd-principal strain':616,
    }

    #If there are additional fringe plots you want then add them here
    valid_plots = {
        'fringe', #Frin
        'isosurf', #
        'contour', #Toggle Line Contours on and off
        'isofringe'
    }

    if plot not in valid_plots:
        warnings.warn('The selected plotting option is not in the selection. Please check that your chosen plot option is in LS-Dyna PrePost')
    
    contour_val = contour_dic[contour] if isinstance(contour,str) else contour
    comment_name = contour
    if isinstance(contour,int) and name is not None:
        comment_name = name

    p_plot = 'p'+plot

    comment = f'$# Plotting {comment_name}\n'    
    return comment + f'{plot} {contour_val}; {p_plot}'
    


def contourRange(crange,min =None,max = None,levels = 10):
    crange_opt = {
    'dynamic':'dynamic',
    'static':'static',
    'user':'userdef',
    'show': 'showelem'
    }

    if crange not in crange_opt.keys():
        raise ValueError(f'Please Enter a Valid range from {crange_opt}')


    if crange in {'dynamic','static'}:
        return f'range {crange_opt[crange]};\nrange level {levels};range pal update;'
    else:
        if min is None or max is None:
            raise ValueError(f'the option {crange} requires a minimum and a maximum range')
        return f'crange {crange_opt[crange]} {min} {max};\nrange level {levels};range pal update;'

    

def rangeOptions(**kwargs):
    '''
    Option for all the other options in range settings.
    **kwatgs means add any keyword arguments to the functions

    e.g. rangeOptions(identmax = 1)

    The variable name is set with the value. So the above example will add the option

    range identmax 1

    to the cfile (which will show the highest stress at the node)

    if an options has more than one input then it must be placed as a tuple or list

    e.g. rangeOptions( fringelimit = (lower_on upper_off))

    '''
    options = []
    for name,setting in kwargs.items:
        option = 'range {name} '
        
        if isinstance(setting,tuple) or isinstance(setting,list):
            for s in setting:
                option += str(s) +' '
        else:
            option += str(setting)
        

        options.append(option+';')
        
    return options

            

    



if __name__ == '__main__':
    print(plotContour(contour='x-displacement', plot = 'fringe'))