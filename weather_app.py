import tkinter as tk
from weather_api import WeatherAPI

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("天气预报")

        self.api_key = '2c0e851252b05fd60a944b5777f49631'  
        self.weather_api = WeatherAPI(self.api_key)

        self.city_label = tk.Label(root, text="城市：")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.get_weather_btn = tk.Button(root, text="获取天气", command=self.get_weather)
        self.get_weather_btn.pack()

        self.weather_info_label = tk.Label(root, text="")
        self.weather_info_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            data = self.weather_api.get_weather_data(city)
            if data['cod'] == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                weather_info = f"天气情况：{weather_description}\n温度：{temperature}℃\n湿度：{humidity}%"
                self.weather_info_label.config(text=weather_info)
            else:
                self.weather_info_label.config(text="获取天气信息失败")
        else:
            self.weather_info_label.config(text="请输入城市名")

if __name__ == "__main__":
    root = tk.Tk()
    weather_app = WeatherApp(root)
    root.mainloop()
