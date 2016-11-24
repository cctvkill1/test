
import asyncio

async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

# get EventLoop:
loop = asyncio.get_event_loop()
# exec coroutine
loop.run_until_complete(hello())
loop.close()