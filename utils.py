import logging
import config
import aiohttp

async def fetch_from_google(origin, destination, mode = None, waypoints = None):
    url = f"https://maps.googleapis.com/maps/api/directions/json?destination={destination}&origin={origin}&key={config.GOOGLE_API}"
    if (mode is not None):
        url+=f"&mode={mode}"
    if (waypoints is not None):
        url += f"&waypoints=optimize:true|{waypoints}"
    return await fetch_data(url)

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
