import aiohttp

class SwearChecker:
    def __init__(self):
        # This pulls from your .env file
        self.url = "https://ai-throughput.vercel.app"

    async def check_text(self, text):
        if not self.url:
            print("Error: VERCEL_API_URL not set!")
            return "0"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.url, json={"content": text}) as resp:
                    if resp.status == 200:
                        return await resp.text()
                    return "2"
            except Exception as e:
                print(f"Vercel API Error: {e}")
                return "0"