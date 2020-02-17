import discord
from config import *
from rvn import *

import discord
from discord.ext import commands

prefix = ">"
client = commands.Bot(command_prefix = PREFIX)

client.remove_command("help")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.command()
async def help(ctx):
    await ctx.send('''```
>help                This command
>helprpc <command>   Get details on RPC command
>blockchain          Get blockchain details
>price               Get price of RVN in satoshis
```''')

@client.command()
async def blockchain(ctx):
    await ctx.send(blockchain_info())

@client.command()
async def helprpc(ctx, command):
    await ctx.send(get_help(command))

@client.command()
async def price(ctx):
    await ctx.send(get_price())

client.run(TOKEN)