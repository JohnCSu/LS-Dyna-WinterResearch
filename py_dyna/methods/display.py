
def displayParts(parts):
    '''
    Takes in either string specifying the part or a list or tuple of parts to display.
    as Partnames are arbitary, you will need to map these to their corresponding partIDs for PrePost

    for solids: S# where # is the part ID
    for Fluids: F# where # is the part ID 

    e.g. for an ALE simulation, the Valve maps to S4 while the fluid is F7

    Inputs:
    parts: str or list/tuple of str. displays the chosen parts.

    examples 
    parts = 'S4'
    parts = ['S4','F7']

    '''
    
    if isinstance(parts,str):
        return f'selectpart on {parts}/0'
    elif isinstance(parts,list) or isinstance(parts,tuple):
        #Bit of python magic here
        return 'selectpart on '.join([f'{part}/0 ' for part in parts])


def partColour(id,color,ColorBy = 'PartID'):
    '''
    Set the color for parts by there ID

    id: str or list of str: parts id(s) to color
    color: a tuple of floats or int (r,g,b) values range from 0 to 255, values exceeding 255 are set to 255 and min is set to 0

    ColorBy: str : Type of ID to color by. Currently only PartID is available
    '''
    r,g,b = [ max(min(c/255,1),0) for c in color]
    s = f'color option 1\ncolor global {r::.2f} {g::.2f} {b::.2f}\n'

    if isinstance(id,str):
        return s + f'genselect part add part {id}/0'
    elif isinstance(id,list) or isinstance(id,tuple):
        #Bit of python magic here
        return s+'genselect part add part '.join([f'{i}/0 ' for i in id])
    

def partTransparency(id,transparency,ColorBy = 'PartID'):
    '''
    Set the transparency for parts by there ID

    id: str or list of str: parts id(s) to color
    transparency: floats ranging from 0 to 1. Set to 1 for invisible and 0 for Opaque

    ColorBy: str : Type of ID to color by. Currently only PartID is available
    '''


    s = f'color option 2\ntransp global {transparency}\n'

    if isinstance(id,str):
        return s + f'genselect part add part {id}/0'
    elif isinstance(id,list) or isinstance(id,tuple):
        #Bit of python magic here
        return s + 'genselect part add part '.join([f'{i}/0 ' for i in id])
    