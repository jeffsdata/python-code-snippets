import discord
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = discord.utils.get(client.get_all_channels(), name="general")
    await channel.send("onready message test")

@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))

    if message.content.startswith('$hello'):
        await message.channel.send('Hello back to you!')

    if(message.content.startswith("$testchannel")):
        channel = discord.utils.get(client.get_all_channels(), name="general")
        await channel.send("channel message test")

    if(message.content.startswith("$testdm")):
        channel = discord.utils.get(client.get_all_channels(), name="general")
        await channel.send("Okay! Sending message to user.")
        
        # Dependent on message
        await message.author.send('👀 I SEE YOU (author).')

        # Independent of message
        guild = client.get_guild(id=827628491590860870) 
        user = guild.get_member(user_id=221457952802865152)
        await user.send('👀 I SEE YOU (user).')

client.run(os.getenv("REDOXBOT_DISCORDCLIENT"))
