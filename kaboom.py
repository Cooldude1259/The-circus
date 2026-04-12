import discord
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Discord client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Yipeee!! The circus is live! Logged in as {client.user}')

@client.event
async def on_message(message):
    print("Message received: ", message.content)
    if message.content.startswith('!kaboom'):
        await message.channel.send('!kaboom')

# Run the Circus
api_key = os.getenv("DISCORD_TOKEN")

client.run(api_key)