import aiohttp


class RequestClient:
    """The HTTP request client"""

    def __init__(self):
        self.session = aiohttp.ClientSession(headers={
            "User-Agent": "awersli99/discordbio.py"
        }, )

    async def make_request(self, endpoint, params=None):
        """Makes an asynchronous http get request"""
        async with self.session.get(endpoint, params=params) as resp:
            return await resp.json(), resp.status

    async def close(self):
        """Closes request client"""
        await self.session.close()
