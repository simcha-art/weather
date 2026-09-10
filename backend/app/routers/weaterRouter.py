from fastapi import APIRouter
from pydantic import BaseModel
import requests

base_url = "https://api.open-meteo.com/v1/forecast?"

router = APIRouter(prefix="/weater", tags=["weater"])

@router.get("/current")
def get_current_weather(latitude: str, longitude: str):

    params = {
        "timezone": "auto",
        "current": "rain,wind_speed_10m,temperature_2m",
        "latitude": latitude,
        "longitude": longitude,
    }

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
def get_forecast_weather(latitude: str, longitude: str, forecast_days: int = 7):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_min,temperature_2m_max,uv_index_max,rain_sum,wind_speed_10m_max",
        "forecast_days": forecast_days,
        "timezone": "auto"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    units = data["daily_units"]
    days = data["daily"]["time"]
    min_temp = data["daily"]["temperature_2m_min"]
    max_temp = data["daily"]["temperature_2m_max"]
    uv_index_max = data["daily"]["uv_index_max"]
    rain_sum = data["daily"]["rain_sum"]
    wind_speed_10m_max = data["daily"]["wind_speed_10m_max"]
    weather = {}
    for i in range(len(days)):
        weather[f"day_{i + 1}"] = {
            "date": days[i], 
            "min_temp": f"{min_temp[i]} {units["temperature_2m_min"]}",
            "max_temp": f"{max_temp[i]} {units["temperature_2m_max"]}",
            "max_uv_index": f"{uv_index_max[i]}",
            "rain_sum": f"{rain_sum[i]}, {units["rain_sum"]}",
            "wind_speed": f"{wind_speed_10m_max[i]} {units["wind_speed_10m_max"]}"
            }
    return weather

