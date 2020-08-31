from typing import Optional, List
from .discord_connection import DiscordConnection

class UserConnections:
    """Contains all of a user's profile connections"""
    website: Optional[str]
    instagram: Optional[str]
    snapchat: Optional[str]
    linkedin: Optional[str]
    discord: List[DiscordConnection]

    def __init__(self, obj: dict, discord: list = []) -> 'UserConnections':
        assert isinstance(obj, dict), 'Received malformed payload from discord.bio API'
        self.website = obj.get("website", None)
        self.instagram = obj.get("instagram", None)
        self.snapchat = obj.get("snapchat", None)
        self.linkedin = obj.get("linkedin", None)
        self.discord = [DiscordConnection(c) for c in discord]