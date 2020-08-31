# pydiscordbio ![PyPI - Downloads](https://img.shields.io/pypi/dw/pydiscordbio) ![PyPI](https://img.shields.io/pypi/v/pydiscordbio)

An unofficial asynchronous Python wrapper for the [discord.bio](https://discord.bio) api.

### Installing

```
pip install pydiscordbio
```

### Usage

* Setting up the client
> This will be used to make requests to the API

```py
from pydiscordbio import Client

client = Client()
```

* Exceptions

| Error | Description |
| ----- | ----------- |
| pydiscordbio.exceptions.APIError | Raised when the request to the API itself fails |
| pydiscordbio.exceptions.NotFound | Raised when the request to the API returns status code 404 |
| pydiscordbio.errors.UserNotFound | Raised when a user doesn't exist in the API |

* Getting a user's details, discord info and connections via username or Discord ID
> All methods of Client are typed meaning your IDE should auto complete the attributes

```py
user = await client.user("wa")
#or
user = await client.user(738128655145762949)
```

* Getting a specific value from a user's details, e.g. description or a users banner URL

```py
description = (await client.user("wa")).details.description

banner_url = (await client.user("wa")).details.banner
```

* Getting a specific value from a user's Discord, e.g. discord ID or username

```py
description = (await client.user("wa")).discord.id

banner_url = (await client.user("wa")).discord.username
```

* Getting a user's connected website

```py
website = (await client.user("wa")).connections.website

# Discord connections
discord_connections = (await client.user("wa")).connections.discord
# Returns a list of DiscordConnection objects
```

* Miscellaneous Endpoints

```py
top_users = await client.top() 
# Returns a list of PartialUser objects
```

### Attributes

* UserDetails (from client.user)
```py
details: User
discord: Discord
connections: UserConnections
```

* User
```py
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
```

* Discord
```py
id: int
username: str
full_username: str
avatar: Optional[str]
avatar_url: str
is_avatar_animated: bool
discriminator: str
flags: int
```

* UserConnections
```py
website: Optional[str]
instagram: Optional[str]
snapchat: Optional[str]
linkedin: Optional[str]
discord: List[DiscordConnection]
```

* PartialUser
```py
slug: str
verified: bool
staff: bool
premium: bool
likes: int
description: Optional[str]
discord: Discord
```

* DiscordConnection
```py
connection_type: str
name: str
id: str
```
