import asyncio
import time

@asyncio.coroutine
def wget(host):
    st = time.time()
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain() 
    line = yield from reader.readline() 
    print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close() 
    et = time.time()
    print('耗时',et-st)

print('协程--单线程异步io')
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.zhongyulian.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print('3个连接由一个线程通过coroutine并发完成')
