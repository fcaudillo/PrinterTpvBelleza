import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from escpos.printer import Usb
from escpos.constants import *

p = Usb(0x04b8,0x0202)

# font = ImageFont.truetype("Arial-Bold.ttf",14)
font = ImageFont.truetype("/home/francisco/gunplay3.ttf",50)


precio = "$30.00"
codigo_barras='1324354657687'
descripcion_producto='123456789 123456789 123456789 123456789'

#Calcular el ancho y alto del font
imgFont=Image.new("RGBA",(400,200),(255,255,255));
drawFont=ImageDraw.Draw(imgFont)
WF,HF = drawFont.textsize(precio,font=font)
deltaHF = int(round((HF * 0.40)))
#Calcular el tamano del lienzo para dibujar
W,H = (WF+4,HF+deltaHF)
img=Image.new("RGBA", (W,H),(255,255,255))
draw = ImageDraw.Draw(img)
#Dibujar el precio
draw.text(((W-WF)/2,1),precio,(0,0,0),font=font)
#Dibujar un recuadro dentro de la imagen.
#draw.rectangle(((0, 0), (W-1, H-1)),outline="red")
img.save("a_test.png")

p.text(descripcion_producto + "\n")
p.barcode(codigo_barras,'EAN13',64,2,'','')
p.image("a_test.png")
p.barcode(codigo_barras,'EAN13',34,2,'','')
#p.cut(mode='FULL',feed=False)
#El origininal tenia. self._raw(b"\n\n\n\n\n\n")
#Cortar el papel y corregir fix con saltos de linea.
p._raw(b"\n\n\n\n\n")
p._raw(PAPER_FULL_CUT)



