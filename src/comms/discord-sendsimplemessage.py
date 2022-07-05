from email import message
import os
from dotenv import find_dotenv, load_dotenv
import discord

class RedoxBot:
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        pass

    def send_message(self, messagetext):
        intents = discord.Intents.default()
        intents.members = True

        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            guild = client.get_guild(id=827628491590860870) 
            user = guild.get_member(user_id=221457952802865152)
            await user.send(messagetext)
            try:
                await client.close()
            except:
                pass

        client.run(os.getenv("REDOXBOT_DISCORDCLIENT"))


def main():
    rb = RedoxBot()
    rb.send_message("Hello, a real-ish test!")

if __name__ == '__main__':
    main()