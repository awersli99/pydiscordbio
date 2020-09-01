from .request import RequestClient
from .models.user_details import UserDetails
from .models.partial_user import PartialUser
from .exceptions import UserNotFound, APIError, NotFound, InvalidSearch


class Client:
    """The pydiscordbio client"""

    def __init__(self, base_url='https://api.discord.bio/'):
        self.request_client = RequestClient()
        self.base_url = base_url

    async def user(self, identifier):
        """Returns a UserDetails object from a specified identifier"""
        details, status = await self.request_client.make_request(
            endpoint=f'{self.base_url}user/details/{str(identifier)}')
        if status == 404:
            raise UserNotFound('User could not be found')
        if status != 200:
            raise APIError('There was an error with the API')
        return UserDetails(details['payload'])

    async def top(self):
        """Returns a list of PartialUser objects from the top liked profiles"""
        top, status = await self.request_client.make_request(
            endpoint=f'{self.base_url}user/top')
        if status == 404:
            raise NotFound('Page could not be found')
        if status != 200:
            raise APIError('There was an error with the API')
        return [PartialUser(u) for u in top['payload']['users']]

    async def search(self, query: str):
        """

        Returns a list of PartialUser objects from a query

        This is in the order returned by the API

        """
        if len(query) == 0:
            raise InvalidSearch('Query length must be higher than 0')
        search, status = await self.request_client.make_request(
            endpoint=f'{self.base_url}user/search/{str(query)}')
        if 'message' in search:
            return []
        if status == 404:
            raise NotFound('Page could not be found')
        if status != 200:
            raise APIError('There was an error with the API')
        return [PartialUser(u) for u in search['payload']]

    async def close(self):
        """Manually closes request client"""
        await self.request_client.close()
