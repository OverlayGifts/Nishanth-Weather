# weather.py

import requests

def get_weather(city):
    API_KEY = 'ad142619439cc8efa92fab327198f2ec'
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        result = f"""
📍 **{data['name']}, {data['sys']['country']}**
🌤️ Condition: {data['weather'][0]['description'].title()}
🌡️ Temperature: {data['main']['temp']}°C  
💧 Humidity: {data['main']['humidity']}%  
🌬️ Wind Speed: {data['wind']['speed']} m/s
        """
        return result.strip()
    else:
        return "❌ City not found or error fetching data. Please try again."
