import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    def get_weather_data(self, city):
        complete_url = f"{self.base_url}q={city}&appid={self.api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        return data
