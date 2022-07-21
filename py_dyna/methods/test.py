

def test(x,y,z):
    return(locals())
    
local=(test(1,2,3))
print(test(**local))