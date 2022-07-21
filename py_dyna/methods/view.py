def viewpoint(view = 'top'):
    '''
    Set default viewing angle for the GUI

    Valid Views:
        'top','bottom','front','back','left','right','isometric x','isometric y','isometric z'
    '''
    
    valid_views = {'top','bottom','front','back','left','right','isometric x','isometric y','isometric z'} #Need to check


    if view in valid_views:
        return view
    else:
        raise ValueError(f'view give is invalid. Check spelling or please choose a view from the following options: \n{valid_views}')








def rotate(angle = 10,axis = 'X'):
    '''
    
    quart a tuple (x,i,j,k) represent quartinion rotation
    Only occurs if quart is not none (as overloading not really a thing in python ....)

    '''

    axis = axis.lower()
    valid_axis = {'x','y','z'}

    if not (isinstance(angle,float) or isinstance(angle,int)):
        raise ValueError('Enter a number (int or float) for angle')

    if axis not in valid_axis:
        raise ValueError('valid Axis\' are x,y or z')

    return f'r{axis} {angle}'
    



def quat(x,i,j,k):
    #Set Quarternion value
    for q in [x,i,j,k]:
        if not isinstance(int,q) or not isinstance(float,q):
            raise ValueError('quarternion values must be type int or float')
    return f'quat {x} {i} {j} {k};'





def zoom(x,y,z):
    pass





def state(state_no = 1,increment = False):
    '''
    Set the state/frame of the dsplot
    Currently does not check if a given state number is within the total no. of states. Exceeding the total number of from resets state to 1
    e.g if there are 10 states, saying state 100 will revert state back to 1

    turning increment on will instead increment the current state by the number of frames given. Negative states are allowed 
    '''

    if not isinstance(state_no,int):
        raise ValueError('Please insert an integer')
    inc = ''    
    if increment:
        inc = '+' if np.sign(state_no) >= 0 else '-'
    else:
        if state < 0:
            raise ValueError('Please add a positive state number')
    
    return f'state {inc}{state_no}'
