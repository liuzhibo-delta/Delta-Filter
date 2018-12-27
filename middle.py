from PIL import Image 
import numpy as np 
import goss
import sketch
import convolve
import oldtime 
import color_draw
import lomo 
import SoftGlow 
import dark_light 
import snow 

def processing( filename , filtername , para ):
        
    src_image = Image.open( filename ).convert( 'RGB' )
    if para != None :
        sk = sketch.filter( para )
        cl = color_draw.filter( para )
        sg = SoftGlow.filter( para )
        gs = goss.filter( para )
        lo = lomo.filter( para )
        sn = snow.filter( para )
    else :
        sk = sketch.filter()
        cl = color_draw.filter()
        sg = SoftGlow.filter()
        ge = goss.filter()
        lo = lomo.filter()
        sn = snow.filter()
        
    ani = convolve.filter(  )
    ot = oldtime.filter()
    dl = dark_light.filter() 
    

    filters = { 'sketch':sk , 'old-movie':ot , 'color-draw':cl , 'lomo':lo , 'Anisotropic-diffusion':ani , 'SoftGlow':sg , 'blur' : gs  , 'low key' : dl , 'snow':sn }
    src_image = src_image.resize( ( 300 , 300 ) )
    src_matrix = np.array( src_image , float )
    new_image_matrix = filters[ filtername ].processing( src_matrix )
    new_image_matrix = new_image_matrix.astype( np.uint8 )
    pilImage = Image.fromarray( new_image_matrix )

    return pilImage