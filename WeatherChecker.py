import requests

def get_weather(city):
    """Get weather information for a specified city"""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == '404':
        return 'City not found'
    else:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        return f'Temperature: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa\nDescription: {description}'

# Example usage:
print(get_weather('New York'))
