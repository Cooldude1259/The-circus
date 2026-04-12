from api_helper import SwearChecker

# Initialize the helper once
checker = SwearChecker()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Call the helper function
    # result will be the text response from Vercel (e.g., "1" or "0")
    result = await checker.check_text(message.content)

    if "1" in result:
        print(f"Swear detected in: {message.content}")
        # Insert your timeout/delete logic here