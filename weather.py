import requests

def fetch_weather(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data. Please check your location.")

def main():
    api_key = "5eef27d4eb63a34540b87dd70d777807"  
    location = input("Enter a city name: ")
    weather_data = fetch_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()