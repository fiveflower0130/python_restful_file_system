import requests
import asyncio
from aiohttp import ClientSession

base_url = 'http://127.0.0.1:5000/file/'


async def count():
    for i in [1, 2, 3, 4, 5]:
        print(i)
        await asyncio.sleep(1)


async def test_get_path(path):
    endpoint = base_url+path
    print(f'Getting start with {endpoint}')

    async with ClientSession() as session:
        async with session.get(endpoint) as response:
            response = await response.json()
            print(response)


async def main():
    await asyncio.gather(count(), test_get_path('path/to/'), test_get_path('path/to/README.md'))
    # resp = requests.get(endpoint)
    # data = resp.json()
    # print(data)

asyncio.run(main())
print('Finished!')
# test_get_path('path/to/README.md')
# print('test1 Finished!')
# test_get_path('path/to/test.txt')
# print('test2 Finished!')
# test_get_path('path/to/')
# print('test3 Finished!')
