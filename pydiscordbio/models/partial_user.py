from typing import Optional
from .discord import Discord


class PartialUser:
    """A user consisting of partial data similar to :class:`User` and full version of :class:`Discord`"""
    slug: str
    verified: bool
    staff: bool
    premium: bool
    likes: int
    description: Optional[str]
    discord: Discord

    def __init__(self, obj: dict) -> 'None':
        assert isinstance(
            obj, dict), 'Received malformed payload from discord.bio API'
        user = obj.get('user', {})
        discord = obj.get('discord', {})
        self.slug = user.get('slug')
        self.verified = bool(user.get('verified', 0))
        self.staff = user.get('staff', False)
        self.premium = user.get('premium_status', False)
        self.likes = user.get('likes', 0)
        self.description = user.get("description", None)
        self.discord = Discord(discord)
