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
        if isinstance(discord, list):
            self.discord = [DiscordConnection(c) for c in discord]
        else:
            self.discord = []

        if isinstance(obj, dict):
            self.website = obj.get("website", None)
            self.instagram = obj.get("instagram", None)
            self.snapchat = obj.get("snapchat", None)
            self.linkedin = obj.get("linkedin", None)
        else:
            self.website = None
            self.instagram = None
            self.snapchat = None
            self.linkedin = None
