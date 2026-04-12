import discord
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Discord client
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Yipeee!! The circus is live! Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.content.startswith('!kaboom'):
        await message.channel.send('!kaboom')

# Run the Circus
api_key = os.getenv("DISCORD_TOKEN")

bot.run(api_key)