import requests

def get_weather(city):
    api_key = "Your_Actual_API_Key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = {
            "Temperature": f"{data['main']['temp']} k",
            "Humidity": f"{data['main']['humidity']}%",
            "Weather Condition": data['weather'][0]['description']
        }
        return weather
    else:
        print("Error: City not found.")
        return None

def main():
    city = input("Enter city name:")
    weather = get_weather(city)
    if weather:
        print("Weather Information for",city)
        for key,value in weather.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()