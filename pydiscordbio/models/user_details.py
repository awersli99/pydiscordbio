from .user import User
from .discord import Discord
from .user_connections import UserConnections


class UserDetails:
    """A discord.bio user object"""
    details: User
    discord: Discord
    connections: UserConnections

    def __init__(self, obj: dict) -> 'None':
        assert isinstance(
            obj, dict), 'Received malformed payload from discord.bio API'
        self.details = User(
            obj.get("user", {}).get("details", None))
        self.discord = Discord(obj.get("discord"))
        self.connections = UserConnections(obj.get("user", {}).get(
            "userConnections"), obj.get("user", {}).get("discordConnections"))
