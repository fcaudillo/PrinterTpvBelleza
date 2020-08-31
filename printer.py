from escpos.printer import Usb
p = Usb(0x04b8,0x0202)
p.text("Hello World\n")
p.cut()
p.text("Saludos Mexico\n")
p.barcode('1324354657687','EAN13',34,2,'','')
 p.set(font='c')
p.cut()

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from escpos.printer import Usb
p = Usb(0x04b8,0x0202)

# font = ImageFont.truetype("Arial-Bold.ttf",14)
font = ImageFont.truetype("/home/francisco/gunplay3.ttf",110)
img=Image.new("RGBA", (300,120),(255,255,255))
draw = ImageDraw.Draw(img)
draw.text((0, 0),"$30.00",(0,0,0),font=font)
draw = ImageDraw.Draw(img)
img.save("a_test.png")
p.barcode('1324354657687','EAN13',34,2,'','')
p.image("a_test.png")
p.cut()
