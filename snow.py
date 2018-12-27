import numpy as np 
import random 
from scipy.ndimage import filters
from PIL import Image

class filter:
    def __init__( self , para = 0 ):
        self.para = para 

    def processing( self , image ):
        r = image[ : , : , 0 ]
        g = image[ : , : , 1 ]
        b = image[ : , : , 2 ]

        random_image = np.zeros( r.shape )

        for i in range( random_image.shape[ 0 ] ) :
            for j in range( random_image.shape[ 1 ] ) :
                random_image[ i , j ] = random.randint( 0 , 255 )

        random_image = filters.gaussian_filter( random_image , 1 )

        for i in range( random_image.shape[ 0 ] ) :
            for j in range( random_image.shape[ 1 ] ) :
                random_image[ i , j ] = self.adjust( random_image[ i , j ] )

        random_image = filters.gaussian_filter( random_image , 1 )


        r = 255 * ( 1 - ( 1 - r/255 )*( 1 - random_image/255 ) )
        g = 255 * ( 1 - ( 1 - g/255 )*( 1 - random_image/255 ) )
        b = 255 * ( 1 - ( 1 - b/255 )*( 1 - random_image/255 ) )
        
        return np.dstack( [ r , g , b ] )


    def adjust( self , pix ):
        high = 205 + self.para 
        low = 165 - self.para
        
        if pix < low :
            return 0 
        elif pix > high :
            return 255
        else :
            return ( pix - low ) / ( high - low ) * 255