
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

    r,g,b = [c/255 for c in color]
    s = f'color option 1\ncolor global {r::.2f} {g::.2f} {b::.2f}\n'

    if isinstance(id,str):
        return s + f'genselect part add part {id}/0'
    elif isinstance(id,list) or isinstance(id,tuple):
        #Bit of python magic here
        return 'genselect part add part '.join([f'{i}/0 ' for i in id])
    

def partTransparency(id,transparency,ColorBy = 'PartID'):

    s = f'color option 2\ntransp global {transparency}\n'

    if isinstance(id,str):
        return s + f'genselect part add part {id}/0'
    elif isinstance(id,list) or isinstance(id,tuple):
        #Bit of python magic here
        return 'genselect part add part '.join([f'{i}/0 ' for i in id])
    