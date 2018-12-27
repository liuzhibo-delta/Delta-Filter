import numpy as np 

class filter:
    def __init__( self , para = None ):
        self.para = para  
    
    def processing( self , img ):
        trans = np.array([[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]).transpose()
        ret_im = np.dot( img , trans )
        im_max = ret_im.max() 
        im_min = ret_im.min()
        for i in range( ret_im.shape[ 0 ] ):
            for j in range( ret_im.shape[ 1 ] ) :
                for k in range( ret_im.shape[ 2 ] ) :
                    ret_im[ i , j , k ] = ( ret_im[ i , j , k ] - im_min ) * 255 / ( im_max - im_min ) 
        return ret_im 

        
        return ret_im 