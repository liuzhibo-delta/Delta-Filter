import numpy as np
from random import * 
class filter:
    def __init__( self , para = 20 ):
        self.para = para 

    def processing( self , img ):
        r = img[ : , : , 0 ]
        g = img[ : , : , 1 ]
        b = img[ : , : , 2 ]

        r = self.filting( r , 1 ) 
        g = self.filting( g , 2 )
        b = self.filting( b , 3 )

        return np.dstack( [ r , g , b ] )

    def filting( self , img , index ):
        new_r = np.zeros( img.shape )
        for i in range( 1 , img.shape[ 0 ] - 1 ) :
            for j in range( 1 , img.shape[ 1 ] - 1 ) :
                diff = abs( img[ i + 1 , j + 1 ] +  img[ i - 1 , j - 1 ] - 2 * img[ i , j ] )
                if diff > self.para  :
                    new_r[ i , j ] = new_r[ i , j ]
                else :
                    new_r[ i , j ] = 255 

        return new_r  

