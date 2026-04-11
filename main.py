import os
import threading
import discord
import requests
from flask import Flask
from discord.ext import commands

# 1. Setup Flask for Render's Health Check
app = Flask(__name__)

@app.route('/health')
def health_check():
    return "Bot is alive!", 200

def run_flask():
    # Render provides the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Setup Discord Bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required to read message text

bot = commands.Bot(command_prefix="!", intents=intents)

VERCEL_API_URL = "https://your-project.vercel.app/api/check-swear"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Call your Vercel API
    try:
        response = requests.post(VERCEL_API_URL, json={"text": message.content})
        data = response.json()

        if data.get("is_swear"):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please watch your language!")
    except Exception as e:
        print(f"Error calling API: {e}")

    await bot.process_commands(message)

# 3. Start both services
if __name__ == "__main__":
    # Run Flask in a separate thread
    t = threading.Thread(target=run_flask)
    t.start()
    
    # Run the Bot in the main thread
    bot.run(os.environ.get("DISCORD_TOKEN"))