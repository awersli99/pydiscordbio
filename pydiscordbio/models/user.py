from datetime import datetime
import dateutil.parser
from typing import Optional

GENDER = {
    0: "Male",
    1: "Female"
}


def from_datetime(x: str) -> Optional[datetime]:
    """Returns a parsed datetime object."""
    try:
        return dateutil.parser.parse(x)
    except ValueError:
        return None


class User:
    """A discord.bio user object"""
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
