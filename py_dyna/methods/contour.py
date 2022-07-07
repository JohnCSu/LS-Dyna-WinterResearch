

def plotContour(contour = 'x_stress', name = None):
    '''
    Plot the contour of the model.

    LS-dyna uses integers to map to field contours. For example,
    x-stress is keyed 1
    y-stress is keyed to 2 etc.

    Inputs
        Contour: type str of int

            String: returns the contour output listed in the dictionary below

            Int: instead of using a string, use the field key directly. This can be
                used to plot contours not listed in the dictionary below


        Name (Optional): Only used if contour is an int
            ignored if contour is a string
            String: gives a name to the new contour



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

    }

    contour_val = contour_dic[contour] if isinstance(contour,str) else contour

    if isinstance(contour,str) or name is None:
        comment_name = contour
    else:
        comment_name = name
 
    comment = f'#$ Plotting {comment_name}\n'    
    return comment + f'fringe {contour_val}; pfringe'
    


def FringeOptions(**kwargs):
    pass



if __name__ == '__main__':
    print(plotContour(contour='x-displacement'))