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

def on_open(self): 
    try: 
        def run(*args):
            # print (args[0])
            self.send("{'event':'addChannel','channel':'"+args[0]+"','binary':'true'}")

        threads = []
        channels = ['ok_sub_spotusd_btc_ticker','ok_sub_futureusd_btc_ticker_this_week','ok_sub_futureusd_btc_ticker_next_week','ok_sub_futureusd_btc_ticker_quarter','ok_sub_futureusd_btc_index'] 
        for x in range(len(channels)):    
            # print(x)
            thread = Thread(target=run, args=(channels[x],))
            threads.append(thread)
            thread.start()  
        for thread in threads:
                thread.join()    
    except Exception as e:
        print (e)   
 
def on_message(self,evt):
    data = inflate(evt)  
    data = str(data, "utf-8")
    json_dict = json.loads(data)
    print( json_dict[0]['data']['last'])

def inflate(data):
    decompress = zlib.decompressobj(-zlib.MAX_WBITS)
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def on_error(self,evt):
    print (evt)

def on_close(self):
    print ('DISCONNECT')


def get_data(): 
    try:
        url        = config.url       
        websocket.enableTrace(False) 
        ws         = websocket.WebSocketApp(url,on_message = on_message,on_error = on_error,on_close = on_close)
        ws.on_open = on_open 
        ws.run_forever()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_data();

