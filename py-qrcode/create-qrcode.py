# encoding=utf-8
import qrcode
from PIL import Image


url = 'http://wx341.vshangtong.com/wxapi.php?ac=photo&tid=341&from=timeline&isappinstalled=0'
qr = qrcode.QRCode(  
    version=1,  #参数 version 表示生成二维码的尺寸大小，取值范围是 1 至 40，最小尺寸 1 会生成 37 * 37 的二维码 
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=2,  #参数 box_size 表示二维码里每个格子的像素大小。
    border=0,  #border 表示边框的格子厚度是多少（默认是4）。
)  
qr.add_data(url)  
qr.make(fit=True)    
img = qr.make_image()  
img.save("qrcode.png")  
 
 
#生成带logo 的二维码
# qr = qrcode.QRCode(
#     version=2,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=1
# )
# qr.add_data(url)
# qr.make(fit=True)
 
# img = qr.make_image()
# img = img.convert("RGBA") 
# icon = Image.open("bg.png") 
# img_w, img_h = img.size
# factor = 4
# size_w = int(img_w / factor)
# size_h = int(img_h / factor) 
# icon_w, icon_h = icon.size
# if icon_w > size_w:
#     icon_w = size_w
# if icon_h > size_h:
#     icon_h = size_h
# icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS) 
# w = int((img_w - icon_w) / 2)
# h = int((img_h - icon_h) / 2)
# img.paste(icon, (w, h), icon) 
# img.save("qrcode_logo.png")

 
bgImge  = Image.open('bg.png')  
toImage = Image.new('RGBA',bgImge.size) 
toImage.paste(bgImge, (0,0) )
fromImge = Image.open('qrcode.png')  
# fromImge = fromImge.resize((50,50))
toImage.paste(fromImge, (100,100)) 

toImage.show()