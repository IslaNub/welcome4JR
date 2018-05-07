import aiohttp
headers = {"auth": "a123b4567"}
url = "https://api.royaleapi.com/clan/2CCCP"
async with aiohttp.ClientSession() as session:
    async with session.get(url, headers=headers) as resp:
        data = await resp.json()
