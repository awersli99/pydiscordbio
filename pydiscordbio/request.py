import aiohttp

class RequestClient:
    def __init__(self):
        self.session = aiohttp.ClientSession(headers={
            "User-Agent": "awersli99/discordbio.py v1"
        }, )

    async def make_request(self, endpoint, params=None):
        async with self.session.get(endpoint, params=params) as resp:
            return await resp.json(), resp.status

    
    async def close(self):
        await self.session.close()