from fastapi import APIRouter
import requests

base_url = "https://api.open-meteo.com/v1/forecast?"
params = {"current": "rain,wind_speed_10m,temperature_2m", "timezone": "auto"}

router = APIRouter(prefix="/weater", tags=["weater"])

@router.get("/current")
def get_current_weather(latitude: str, longitude: str):
    params["latitude"] = latitude
    params["longitude"] = longitude
    response = requests.get(base_url, params=params)
    data = response.json()
    data = data["current"]
    weather = {
        "rain": f"{data["rain"]} mm", 
        "wind_speed_10m": f"{data["wind_speed_10m"]} km/h", 
        "temperature_2m": f"{data["temperature_2m"]} °C"
        }
    return weather

@router.get("/forecast")
def get_forecast_weather(latitude: str, longitude: str, forecast_days: int):
    return "not implemented"

@router.get("/compare-cities")
def compare_two_cities(city1: dict, city2: dict, parameters: list):
    return "not implemented"
