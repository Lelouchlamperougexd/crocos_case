import openai
import logging
import config
import aiohttp

async def fetch_from_google(origin, destination, mode):
    return await fetch_data(f"https://maps.googleapis.com/maps/api/directions/json?destination={destination}&origin={origin}&mode={mode}&key={config.GOOGLE_API}")

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

client = openai.AsyncOpenAI(
    api_key=config.OPENAI_TOKEN
)

async def generate_text(prompt) -> dict:
    try:
        chat_completeion = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                 }
            ]
        )
        return chat_completeion['choices'][0].message.content
    except Exception as e:
        logging.error(e)

