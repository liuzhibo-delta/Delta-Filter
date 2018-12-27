from tkinter import *
import tkinter.filedialog
import tkinter.ttk
import time 
from PIL import Image , ImageTk , ImageEnhance
import numpy as np
import middle

pilImage_src = None 
image_src_matrix = None

def select_file():
    global image_src
    global filename , image_src_matrix
    filename = tkinter.filedialog.askopenfilename()
    print( filename )
    pilImage_src = Image.open( filename ).convert('RGB').resize( ( 300 , 300 ) )
    image_src_matrix = np.array( pilImage_src , float )
    pilImage_src_canvas = pilImage_src.resize( ( 300 , 300 ) , Image.ANTIALIAS )
    image_src = ImageTk.PhotoImage( pilImage_src_canvas )
    imagesprite = canvaA.create_image( 150 , 150 ,  image = image_src  )


filtername = 'lomo'

ret_image = None
ret_image_matrix = None 

res_image_matrix = None

brightness = 1.0
constract = 1.0
color = 1.0
image_result = None 

def processing():
    global filename , filtername , ret_image , image_ret_show_tk , ret_image_matrix , image_result
    filtername = combox.get()
    para = int( combox_para.get() )
    ret_image = middle.processing( filename , filtername , para )
    ret_image_matrix = np.array( ret_image , float )
    image_ret_show = ret_image.resize( ( 300 , 300 ) , Image.ANTIALIAS )
    image_result = image_ret_show 
    image_ret_show_tk = ImageTk.PhotoImage( image_ret_show )
    imagesprite_res = canvaB.create_image( 150 , 150 , image = image_ret_show_tk )

def update_view():
    global image_ret_show_tk , image_src_matrix , image_result , imagesprite_res , ret_image_matrix , res_image_matrix , alpha , brightness , constract , color

    res_image_matrix = alpha * image_src_matrix + ( 1- alpha ) * ret_image_matrix 
    res_image_matrix = res_image_matrix.astype( np.uint8 )
    image_result = Image.fromarray( res_image_matrix )
    image_result = ImageEnhance.Brightness( image_result ).enhance( brightness )
    image_result = ImageEnhance.Color( image_result ).enhance( color )
    image_result = ImageEnhance.Contrast( image_result ).enhance( constract )
    image_ret_show = image_result.resize( ( 300 , 300 ) , Image.ANTIALIAS  )
    image_ret_show_tk = ImageTk.PhotoImage( image_ret_show )
    imagesprite_res = canvaB.create_image( 150 , 150 , image = image_ret_show_tk )    

    return 

def update_color( new_value ):
    global color 
    color = float( new_value )
    update_view()
    return 

def update_mix( new_value ):
    global image_ret_show_tk , imagesprite_res , ret_image_matrix , res_image_matrix , alpha
    alpha = 1 - float( new_value )
    update_view()
    return 

def update_brightness( new_value ):
    global res_image_matrix , image_ret_show_tk , imagesprite_res , brightness
    brightness = float( new_value )
    update_view()
    return 

def update_constract( new_value ):
    global constract
    constract = float( new_value ) 
    update_view()
    return    

def save_file():
    path = filename + '.' + filtername + '.png'
    image_result.save( path )
    return 

root = Tk() 
root.geometry( '700x550' )
root.title( 'Delta-Filter' )
canvaA = Canvas( root , width =300 , height =300 )
canvaB = Canvas( root , width =300 , height =300 )
canvaA.place( x = 20 , y = 20 , width =300 , height =300 )
canvaB.place( x = 20 + 300 + 40 , y = 20 , width =300 , height =300 )
button_select_file = Button( root , text = '选择文件' , command = select_file )
button_select_file.place( x = 200 , y = 20 + 40 +300 )
button_processing = Button( root , text = '开始处理' , command = processing )
button_processing.place( x = 200 , y = 20 + 40 +300 + 40 )
button_save_file = Button( root , text = '保存文件' , command = save_file )
button_save_file.place( x = 200 , y = 20 + 40 + 300 + 40 + 40 )
comvalue = tkinter.StringVar()
comvalue = 'delta'
combox = tkinter.ttk.Combobox( root , textvariable = comvalue )
combox[ 'values' ] = ( 'lomo' , 'color-draw' , 'old-movie' , 'sketch' , 'Anisotropic-diffusion' , 'SoftGlow' , 'blur' , 'low key' , 'snow' )
combox.place( x = 20 , y =  20 + 40 +300 + 40 , width = 100 )
combox_para = tkinter.ttk.Combobox( root )
combox_para[ 'values' ] = [ i for i in range( 30 ) ]
combox_para.place( x = 130 , y = 20 + 40 + 300 + 40 , width = 60 )





mix_rate = Scale( root , from_ = 0 , to = 1 , resolution = 0.02 , command = update_mix , orient=HORIZONTAL )
mix_rate.set(1)
mix_rate.place( x =  400  , y =   300 + 40  , width = 150 )
bright_rate = Scale( root , from_ = 0 , to = 2 ,resolution = 0.02 , command = update_brightness , orient = HORIZONTAL )
bright_rate.set(1)
bright_rate.place( x = 400 , y = 300 + 40 + 40 , width = 150 )
constract_rate = Scale( root , from_ = 0 , to = 2 , resolution = 0.02 , command = update_constract , orient=HORIZONTAL )
constract_rate.set(1)
constract_rate.place( x = 400 , y = 300 + 40 + 40 + 40 , width = 150 )
color_rate = Scale( root , from_ = 0 , to = 2 , resolution = 0.02 , command = update_color , orient=HORIZONTAL )
color_rate.set(1)
color_rate.place( x = 400 , y = 300 + 40 + 40 + 40 + 40 , width = 150 )

label_mix = Label( root , text = '滤镜效果' )
label_brightness = Label( root , text = '亮度' )
label_constract = Label( root , text = '对比度' )
label_color = Label( root , text = '色度' )
label_filter = Label( root , text = '选择滤镜' )
label_para = Label( root , text = '设置参数' )


label_mix.place( x = 400 - 70 , y =   300 + 40 +20 )
label_brightness.place( x = 400 - 50 , y =  300 + 40 + 40 + 20 )
label_constract.place( x = 400 - 60 , y =  300 + 40 + 40 + 40 + 20 )
label_color.place( x = 400 - 50 , y = 300 + 40 + 40 + 40 + 40 + 20 )
label_filter.place(  x = 20 + 10 , y = 20 + 40 + 300 + 15 , width = 100 )
label_para.place( x = 130 , y = 20 + 40 + 300 + 15 , width = 60 )

root.mainloop()

