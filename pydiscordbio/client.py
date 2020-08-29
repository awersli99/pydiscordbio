from .request import RequestClient
from .models.user_details import UserDetails
from .exceptions import UserNotFound, APIError


class Client:
    def __init__(self, base_url='https://api.discord.bio/'):
        self.request_client = RequestClient()
        self.base_url = base_url

    async def user(self, identifier: str):
        details, status = await self.request_client.make_request(endpoint=f'{self.base_url}user/details/{identifier}')
        if status == 404:
            raise UserNotFound('User could not be found')
        if status != 200:
            raise APIError('There was an error with the API')
        print(details)
        return UserDetails(details['payload'])

    async def close(self):
        await self.request_client.close()
