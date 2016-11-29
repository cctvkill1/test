import websocket
import time
import sys
import json
import hashlib
import zlib
import base64
import config 
import asyncio 
from threading import Thread
from getDataInMysql import insert_data
 
def on_message(self,evt):
    data = inflate(evt)  
    print(data)
    data = str(data, "utf-8")
    json_dict = json.loads(data)
    channel = json_dict[0]['channel'] 
    if channel == 'ok_sub_spotcny_btc_ticker':
        insert_data('btc_cny',json_dict[0]['data']['last'])  


def inflate(data):
    decompress = zlib.decompressobj(-zlib.MAX_WBITS)
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def on_error(self,evt):
    print (evt)

def on_close(self):
    print ('DISCONNECT')

# 中国站 现货 缺少汇率api
def on_open_cny(self):  
    self.send("{'event':'addChannel','channel':'ok_sub_spotcny_btc_ticker','binary':'true'}") 
 
def get_data_cny():
    try:
        url_cny        = config.url_cny  
        websocket.enableTrace(False) 
        ws_cny         = websocket.WebSocketApp(url_cny,on_message = on_message,on_error = on_error,on_close = on_close)
        ws_cny.on_open = on_open_cny 
        ws_cny.run_forever()
    except Exception as e:
        print(e)

if __name__ == "__main__": 
    get_data_cny();

