import numpy as np
from scipy import signal 
from random import * 
import math 
class filter:
    def __init__( self , para = 1 ):
        self.para = para 

    def processing( self , img ):
        r = img[ : , : , 0 ]
        g = img[ : , : , 1 ]
        b = img[ : , : , 2 ]


        for i in range( 200 ) :
            r = self.filting( r ) 
            g = self.filting( g )
            b = self.filting( b )
            print( i )

        ret_im = np.dstack( [ r , g , b ] )
        im_max = ret_im.max() 
        im_min = ret_im.min()
        for i in range( ret_im.shape[ 0 ] ):
            for j in range( ret_im.shape[ 1 ] ) :
                for k in range( ret_im.shape[ 2 ] ) :
                    ret_im[ i , j , k ] = ( ret_im[ i , j , k ] - im_min ) * 255 / ( im_max - im_min ) 
        return ret_im 

    def g( self , img_new ):
        for i in range( img_new.shape[ 0 ] ) :
            for j in range( img_new.shape[ 1 ] ) :
                img_new[ i , j ] *= 1/( 1 + np.square( img_new[ i , j ] / self.para ) )

    def filting( self , img ) :
        kernel = [ [ 0 , -1 , 0 ] , [ -1 , 4 , -1 ] , [ 0 , -1 , 0 ] ]
        img_new = signal.convolve2d( img , kernel )[ 1 : img.shape[ 0 ] + 1 , 1 : img.shape[ 1 ] + 1  ]
        self.g( img_new )
        img_new  = signal.convolve2d( img_new , kernel )[ 1 : img.shape[ 0 ] + 1  , 1 : img.shape[ 1 ] + 1 ]
        img -= 10 * img_new 
        return img 