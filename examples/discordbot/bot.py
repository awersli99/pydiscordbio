import discord 
from discord.ext import commands
from decouple import config
import pydiscordbio

TOKEN = config('TOKEN')

description = "An example bot to showcase the pydiscordbio api wrapper."

client = commands.Bot(command_prefix='?', description=description)
discordbio = pydiscordbio.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.id}')

@client.command()
async def ping(ctx):
    """Check if the bot is alive."""
    await ctx.send('pong')

@client.command()
async def user(ctx, identifier):
    """Get a user's discord.bio profile details"""
    user = await discordbio.user(str(identifier))
    embed=discord.Embed(title=user.discord.full_username, url=f'https://dsc.bio/{user.details.slug}', description=f"{user.discord.full_username}`({user.discord.username})`", color=0xff0000)
    embed.set_thumbnail(url=user.discord.avatar_url)
    embed.add_field(name=':notepad_spiral: **About**:', value=user.details.description, inline=False)
    embed.add_field(name=':heart: **Likes:**', value=f'{user.details.likes}', inline=False)
    embed.add_field(name=':id: **User ID:**', value=f'{user.discord.id}', inline=False)
    embed.add_field(name=':map: **Location:**', value=f'{user.details.location}', inline=True)
    embed.add_field(name=':birthday: **Birthday:**', value=f'{user.details.birthday}', inline=True)
    embed.add_field(name=':envelope: **Mail:**', value=f'{user.details.email}', inline=True)
    embed.add_field(name=':restroom: **Gender:**', value=f'{user.details.gender}', inline=True)
    embed.add_field(name=':tools: **Occupation:**', value=f'{user.details.occupation}', inline=True)
    embed.add_field(name=':calendar_spiral: **Account Created:**', value=f'{user.details.created_at}', inline=True)
    await ctx.send(embed=embed)

@client.command()
async def top(ctx):
    """Get the top 10 most liked profiles"""
    top_users = await discordbio.top()
    embed = discord.Embed(title='**Top Likes** :heart:', url=f'https://discord.bio/profiles', color=0xff0000)
    for x in top_users[:10]:
        index = top_users.index(x)
        embed.add_field(name=f'**[{index+1}] {x.discord.full_username}**', value=f'{x.likes} likes', inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN)

discordbio.close()
