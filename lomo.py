import numpy as np 
from PIL import Image
import random
import math 
from scipy import stats
from scipy.stats import norm
import SoftGlow

def gaussian(sigma, x, u):
	y = np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
	return y

class filter:
    def __init__( self , para = 2 ):
        self.para = para 
    
    def processing( self , image ):
        sf = SoftGlow.filter( self.para )
        image = sf.processing( image )
        light = np.zeros( ( image.shape[ 0 ] , image.shape[ 1 ] ) )
        start_gray = 1.0 
        end_gray = 0.6
        max_radius = math.sqrt( np.square( image.shape[ 0 ] // 2 ) + np.square( image.shape[ 1 ] // 2 ) )
        for i in range( light.shape[ 0 ] ) :
            for j in range( light.shape[ 1 ] ) :
                radius = math.sqrt( np.square( i - image.shape[ 0 ] // 2 ) + np.square( j - image.shape[ 1 ] // 2 ) )
                light[ i , j ] = end_gray + ( max_radius - radius ) / max_radius * ( start_gray - end_gray ) 
        ret_image = np.zeros( image.shape )
        for i in range( ret_image.shape[ 0 ] ) :
            for j in range( ret_image.shape[ 1 ] ) :
                ret_image[ i , j ] = image[ i , j ] * light[ i , j ]

        base_color = ( 236 , 217 , 120 )
        for i in range( ret_image.shape[ 0 ] ):
            for j in range( ret_image.shape[ 1 ] ):
                for k in range( ret_image.shape[ 2 ] ):
                    ret_image[ i , j , k ] = 0.3 * ( ( ret_image[ i , j , k ] + base_color[ k ] ) - ret_image[ i , j , k ] * base_color[ k ] / 256 ) + 0.7 * ret_image[ i , j , k ] 



        return ret_image