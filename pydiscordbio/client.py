from .request import RequestClient
from .models.user_details import UserDetails, PartialUser
from .exceptions import UserNotFound, APIError, NotFound


class Client:
    """pydiscordbio client"""
    def __init__(self, base_url='https://api.discord.bio/'):
        self.request_client = RequestClient()
        self.base_url = base_url

    async def user(self, identifier):
        """Returns a UserDetails object from a specified identifier"""
        details, status = await self.request_client.make_request(endpoint=f'{self.base_url}user/details/{str(identifier)}')
        if status == 404:
            raise UserNotFound('User could not be found')
        if status != 200:
            raise APIError('There was an error with the API')
        return UserDetails(details['payload'])

    async def top(self):
        """Returns a list of PartialUser objects from the top liked profiles"""
        top, status = await self.request_client.make_request(endpoint=f'{self.base_url}user/top')
        if status == 404:
            raise NotFound('Page could not be found')
        if status != 200:
            raise APIError('There was an error with the API')
        return [PartialUser(u) for u in top['payload']['users']]

    async def close(self):
        """Closes request client"""
        await self.request_client.close()
