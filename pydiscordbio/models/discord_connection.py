class DiscordConnection:
    """A discord connection object"""
    connection_type: str
    name: str
    id: str

    def __init__(self, obj: dict) -> 'DiscordConnection':
        assert isinstance(obj, dict), 'Received malformed payload from discord.bio API'
        self.connection_type = [*obj][0]
        self.name = obj.get([*obj][0]).get("name")
        self.id = obj.get([*obj][0]).get("id")