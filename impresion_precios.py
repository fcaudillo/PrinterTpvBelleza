#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from escpos.printer import Usb
from escpos.constants import *


# font = ImageFont.truetype("Arial-Bold.ttf",14)
font = ImageFont.truetype("/home/francisco/gunplay3.ttf",50)


precio = "$30.00"
codigo_barras='1324354657687'
descripcion_producto='123456789 123456789 123456789 123456789'

def generar_imagen_font (texto, fuente, filename):
   #Calcular el ancho y alto del font 
   imgFont=Image.new("RGBA",(400,200),(255,255,255));
   drawFont=ImageDraw.Draw(imgFont)
   WF,HF = drawFont.textsize(texto,font=fuente)
   deltaHF = int(round((HF * 0.40)))
   #Calcular el tamano del lienzo para dibujar
   W,H = (WF+4,HF+deltaHF)
   img=Image.new("RGBA", (W,H),(255,255,255))
   draw = ImageDraw.Draw(img)
   #Dibujar el precio
   draw.text(((W-WF)/2,1),texto,(0,0,0),font=fuente)
   #Dibujar un recuadro dentro de la imagen.
   #draw.rectangle(((0, 0), (W-1, H-1)),outline="red")
   img.save(filename)



def genera_boletos (rango):
  font2 = ImageFont.truetype("/home/francisco/Carousel.ttf",60)
  font = ImageFont.truetype("/home/francisco/gunplay3.ttf",120)
  generar_imagen_font('Boleto',font2,'boleto.png')
  p = Usb(0x04b8,0x0202)
  sa = "niñoññ"
  for x in rango:
     nombre_imagen = 'a_number{}.png'.format(x)
     generar_imagen_font(str(x),font,nombre_imagen)
     p.set(align='center',font='b')
     p.charcode(code="NORDIC")
     p.image("FantasyWorld.png")
     p.text("Venta de articulos de belleza,  cosmeticos,  regalos, y  juguetes." + "\n\n")
     p.image("boleto.png")
     p.image(nombre_imagen);
     p.text("Fantasy  les  desea  una  feliz  navidad y prospero anio nuevo\n")
     p.text("La rifa se llevara a cabo el dia 6 de enero del 2018 a  las 12:00 pm\n")
     p.text("Gracias por su preferencia\n")
     p.cut()
     p.image("boleto.png")
     p.image(nombre_imagen);
     p.text("\n________________________________________" + "\n")
     p.text("Nombre\n\n");
     p.set(align='center',font='a')
     p.text("Deposite este boleto en la urna")
     p.cut()


genera_boletos(range(2,30));


font = ImageFont.truetype("/home/francisco/gunplay3.ttf",50)
font2 = ImageFont.truetype("/home/francisco/Carousel.ttf",50)

generar_imagen_font('Boleto',font,'a1.png')
generar_imagen_font('Boleto',font2,'a2.png')




