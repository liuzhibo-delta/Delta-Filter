import numpy as np
from scipy.ndimage import filters


class filter:
    def __init__( self , para = 2 ):
        self.para = para 

    def processing( self , img ):
        '''
        img : a * b * 3
        '''
        red_img = img[: , : , 0]
        green_img = img[: , : , 1]
        blue_img = img[: , : , 2]

        red_img = self.filting( red_img )
        green_img = self.filting( green_img )
        blue_img = self.filting( blue_img ) 

        return np.dstack( [ red_img , green_img , blue_img ] ) 
    
    def filting( self , img ):
        img = filters.gaussian_filter( img , self.para )
        return img 
        
