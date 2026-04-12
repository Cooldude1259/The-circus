import discord
import os
from dotenv import load_dotenv
from api_helper import SwearChecker

# Load environment variables
load_dotenv()

# Initialize the Discord client
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Yipeee!! The circus is live! Logged in as {bot.user}')

# Initialize the helper once
checker = SwearChecker()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    author_id = message.author.id
    author = message.author.name
    chanel = message.channel.name
    content = message.content
    message_id = message.id
    roles = message.author.roles
    if "Abstracted" in [role.name for role in roles]:
        if chanel != "talk-to-the-abstracted":
            await message.delete()
            print(f"Deleted message from {author} in {chanel} for being Abstracted")
            return
        

    # Call the helper function
    # result will be the text response from Vercel (e.g., "1" or "0")
    result = await checker.check_text(message.content)

    if "1" in result:
        print(f"Swear detected in: {message.content}")
        # Insert your timeout/delete logic here
    elif result == "2":
        print("API returned an error status. Please check the API for issues.")
        await message.channel.send("Sorry, I'm having trouble checking that message right now. Please contact <@794832846228684800> for support on this issue.")


# Run the Circus
api_key = os.getenv("DISCORD_TOKEN")

bot.run(api_key)