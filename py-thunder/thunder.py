# -*- coding: utf-8 -*-  
import urllib.parse
import base64
import os

url = 'ftp://7e:7e@d8.3edyy.com:161/【3E电影院www.eee4.cc】叶问2[DVD国语中字].rmvb' 
print('准备下载'+url)
QutoUrl = urllib.parse.quote(('AA'+url+'ZZ').encode('utf-8')) 
downurl= 'thunder://'+(base64.b64encode(bytes(QutoUrl,'utf-8'))).decode('utf-8')
# downurl= 'thunder://'+base64.b64encode(bytes(QutoUrl, 'utf-8'))
os.execl(r"C:\Program Files (x86)\Thunder\Program\Thunder.exe" ,'-StartType:DesktopIcon '+downurl)