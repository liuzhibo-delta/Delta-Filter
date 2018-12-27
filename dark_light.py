import numpy as np 

class filter:
    def __init__( self , para = None ):
        self.para = para 
    
    def processing( self , image ):
        red = image[ : , : , 0 ]
        blue = image[ : , : , 1 ]
        green = image[ : , : , 2 ]

        red = red * red / 256
        blue = blue * blue / 256 
        green = green * green / 256

        return np.dstack( [ red , blue , green ] )
