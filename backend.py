import requests

API_KEY = "a0297e46c385f5b2584d89fff6882515"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_days = 8 * forecast_days
    filtered_data = filtered_data[:num_days]
    return filtered_data

