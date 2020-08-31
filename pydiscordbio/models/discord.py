from typing import Optional

class Discord:
    """Contains all of a user's discord information."""
    id: int
    username: str
    full_username: str
    avatar: Optional[str]
    avatar_url: str
    is_avatar_animated: bool
    discriminator: str
    flags: int

    def __init__(self, obj: dict) -> 'Discord':
        assert isinstance(
            obj, dict), 'Received malformed payload from discord.bio API'
        self.id = int(obj.get("id"))
        self.username = obj.get("username")
        self.avatar = obj.get("avatar", None)
        self.discriminator = obj.get("discriminator")
        self.flags = obj.get("public_flags", 0)

    @property
    def full_username(self) -> str:
        """Returns the user's name and discriminator together, seperated by #"""
        return f'{self.username}#{self.discriminator}'

    @property
    def avatar_url(self) -> str:
        """Returns the user's avatar as either PNG or GIF"""
        if not self.avatar:
            return f'https://cdn.discordapp.com/embed/avatars/' + int(self.discriminator) % 5 + '.png'
        if self.is_avatar_animated:
            return f'https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.gif'
        return f'https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.png'

    @property
    def is_avatar_animated(self) -> bool:
        """Returns true if a user has a gif profile picture"""
        return bool(self.avatar and self.avatar.startswith('a_'))