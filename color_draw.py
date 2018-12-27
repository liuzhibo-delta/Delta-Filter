import numpy as np 

class filter:
    def __init__( self , para = 1 ):
        self.para = para 
    
    def processing( self , image ):
        kernel_size = 2 * self.para + 1 
        gray_img = image[ : , : , 0 ] * 0.333 + image[ : , : , 1 ] * 0.333 + image[ : , : , 2 ] * 0.333 
        gray_img = gray_img.astype( np.uint8 )
        buckets_num = 4
        new_image = np.zeros( image.shape )

        for i in range( image.shape[ 0 ] ) :
            for j in range( image.shape[ 1 ] ) :
                buckets = {}
                for k in range( kernel_size * kernel_size ) :
                    x_index =  i + k // kernel_size - ( kernel_size - 1 )//2 
                    y_index = j + k % kernel_size - ( kernel_size - 1 ) // 2
                    if  x_index in range( 0 , image.shape[ 0 ] ) and y_index in range( 0 , image.shape[ 1 ] ) :
                        gray_value = gray_img[ x_index , y_index ]
                        gray_index = int ( gray_value / 256 * buckets_num ) 
                        if gray_index in buckets :
                            buckets[ gray_index ].append( image[ x_index , y_index ] )
                        else :
                            buckets[ gray_index ] = [ image[ x_index , y_index ] ]
                count = [ len( buckets[ i ] ) if i in buckets else 0  for i in range( buckets_num )  ]
                max_index = count.index( max( count ) )
                color = buckets[ max_index ][ 0 ]
                new_image[ i , j ] = color 
        
        return new_image 





