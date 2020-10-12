import os
import discord
from dotenv import load_dotenv
import random


UserID = {
  "Vikram": 444951824223567882, 
  "Dave T":414576371969556480
}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Vikram_resp = ['🅱ikram']

    Tamik_resp = ['S🅱inotto 🅱a🅱ik']

    if message.author.id==UserID['Vikram']:
        response = random.choice(Vikram_resp)
        await message.channel.send(response)
    if message.content ==UserID['Dave T']:
        response = random.choice(Tamik_resp)
        await message.channel.send(response)

client.run(TOKEN)