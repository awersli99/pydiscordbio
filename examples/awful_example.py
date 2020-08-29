import pydiscordbio
import asyncio


async def print_all(user_id):
    client = pydiscordbio.Client()
    user = await client.user(str(user_id))

    print("\nDetails:\n")

    print(user.details.slug)
    print(user.details.user_id)
    print(user.details.flags)
    print(user.details.verified)
    print(user.details.premium_type)
    print(user.details.created_at)
    print(user.details.description)
    print(user.details.location)
    print(user.details.gender)
    print(user.details.birthday)
    print(user.details.email)
    print(user.details.occupation)
    print(user.details.banner)
    print(user.details.premium)
    print(user.details.staff)
    print(user.details.likes)

    print('\nDiscord:\n')

    print(user.discord.id)
    print(user.discord.username)
    print(user.discord.full_username)
    print(user.discord.avatar)
    print(user.discord.avatar_url)
    print(user.discord.is_avatar_animated)
    print(user.discord.discriminator)
    print(user.discord.flags)

    print('\nUser Connections\n')

    print(user.connections.website)
    print(user.connections.snapchat)
    print(user.connections.linkedin)
    print(user.connections.instagram)

    print('\nDiscord Connections:\n')

    for discord_connection in user.connections.discord:
        print(discord_connection.connection_type)
        print(discord_connection.name)
        print(discord_connection.id)
        print()

    top = await client.top()
    for user in top:
        print(f'{user.discord.full_username}: {user.likes}')

    await client.close()

asyncio.run(print_all('465207798968614923'))
