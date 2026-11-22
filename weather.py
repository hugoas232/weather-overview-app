import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
lat = 30.26
lon = -97.74
response = requests.get("https://api.openweathermap.org/data/2.5/weather?" \
"", params={"lat": lat, "lon": lon, "appid":api_key})
print(response.status_code)
data = response.json()
print(data)