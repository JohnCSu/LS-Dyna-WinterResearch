

def plotContour(contour = 'x_stress'):
    '''
    Plot the contour of the model.

    LS-dyna uses integers to map to field contours. For example,
    x-stress is keyed 1
    y-stress is keyed to 2 etc.

    Inputs
        field: type str of int

        String: returns the contour output listed in the dictionary below

        Int: instead of using a string, use the field key directly. This can be
            used to plot contours not listed in the dictionary below


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

    contour = contour_dic[contour] if isinstance(contour,str) else contour
    return f'fringe {contour}; pfringe'
    


def FringeOptions(**kwargs):
    pass






if __name__ == '__main__':
    print(plotContour(contour='x-displacement'))