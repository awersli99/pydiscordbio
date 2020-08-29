from typing import Optional
from datetime import datetime
import dateutil.parser

GENDER = {
    0: "Male",
    1: "Female"
}


def from_datetime(x: str) -> Optional[datetime]:
    try:
        return dateutil.parser.parse(x)
    except ValueError:
        return None


class Discord:
    """A user's Discord"""
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
        return bool(self.avatar and self.avatar.startswith('a_'))


class User:
    """A discord.bio user"""
    slug: str
    user_id: int
    flags: int
    verified: bool
    premium_type: int
    created_at: datetime
    description: str
    location: str
    gender: int
    birthday: Optional[datetime]
    email: Optional[str]
    occupation: Optional[str]
    banner: Optional[str]
    premium: bool
    staff: bool
    likes: int

    def __init__(self, obj: dict) -> 'User':
        assert isinstance(
            obj, dict), 'Received malformed payload from discord.bio API'
        self.slug = obj.get("slug")
        self.user_id = int(obj.get("user_id"))
        self.flags = int(obj.get("flags"))
        self.verified = bool(obj.get('verified', 0))
        self.premium_type = int(obj.get("premium_type"))
        self.created_at = from_datetime(obj.get("created_at"))
        self.description = obj.get("description")
        self.location = obj.get("location")
        self.gender = GENDER.get(obj.get("gender"), None)
        self.birthday = None
        if obj.get("birthday", None):
            self.birthday = from_datetime(obj.get("birthday"))
        if obj.get("email") == "":
            self.email = None
        else:
            self.email = obj.get("email")
        if obj.get("occupation") == "":
            self.occupation = None
        else:
            self.occupation = obj.get("occupation")
        self.banner = obj.get("banner", None)
        self.premium = obj.get('premium', False)
        self.staff = obj.get('staff', False)
        self.likes = obj.get('likes', 0)


class UserDetails:
    """A discord.bio user object"""
    details: User
    settings: User  # backwards compatibility
    discord: Discord

    def __init__(self, obj: dict) -> 'UserDetails':
        assert isinstance(
            obj, dict), 'Received malformed payload from discord.bio API'
        self.details = self.settings = User(
            obj.get("user", {}).get("details", None))
        self.discord = Discord(obj.get("discord"))
