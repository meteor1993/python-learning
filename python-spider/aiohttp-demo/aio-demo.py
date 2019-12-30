import aiohttp
import asyncio
from datetime import datetime

async def main():
    async with aiohttp.ClientSession() as client:
        html = await client.get('https://www.baidu.com/')
        print(html)

loop = asyncio.get_event_loop()

tasks = []
for i in range(100):
    task = loop.create_task(main())
    tasks.append(task)

start = datetime.now()

loop.run_until_complete(main())

end = datetime.now()

print("aiohttp花费时间为：", end - start)