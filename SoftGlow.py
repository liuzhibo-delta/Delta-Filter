import numpy as np 
from scipy.ndimage import filters

class filter:
    def __init__( self , para = 3 ):
        self.para = para 
    
    def processing( self , img ):

        red_img = img[: , : , 0]
        green_img = img[: , : , 1]
        blue_img = img[: , : , 2]

        red_img = self.filting( red_img )
        green_img = self.filting( green_img )
        blue_img = self.filting( blue_img ) 

        return np.dstack( [ red_img , green_img , blue_img ] ) 
    
    def filting( self , img ):
        new_im = filters.gaussian_filter( img , self.para )
        ret_im = img + new_im - img * new_im / 255 
        return ret_im 