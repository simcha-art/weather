from fastapi import APIRouter, Query
from typing import Annotated
import requests

Latitude = Annotated[float, Query(ge=-90, le=90)]
Longitude = Annotated[float, Query(ge=-180, le=180)]
ForecastDays = Annotated[int, Query(ge=1, le=14)]

base_url = "https://api.open-meteo.com/v1/forecast?"

router = APIRouter(prefix="/weater", tags=["weather"])


@router.get("/current")
def get_current_weather(latitude: Latitude, longitude: Longitude):
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
        "temperature_2m": f"{data["temperature_2m"]} °C",
    }
    return weather


@router.get("/forecast")
def get_forecast_weather(
    latitude: Latitude, longitude: Longitude, forecast_days: ForecastDays = 7
):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_min,temperature_2m_max,uv_index_max,rain_sum,wind_speed_10m_max",
        "forecast_days": forecast_days,
        "timezone": "auto",
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
            "wind_speed": f"{wind_speed_10m_max[i]} {units["wind_speed_10m_max"]}",
        }
    return weather


@router.post("/compare")
def compare_cities(
    latitude1: Latitude,
    longitude1: Longitude,
    latitude2: Latitude,
    longitude2: Longitude,
    forecast_days: ForecastDays = 7,
):
    city1 = get_forecast_weather(latitude1, longitude1, forecast_days)
    city2 = get_forecast_weather(latitude2, longitude2, forecast_days)
    compare = {}
    for i in range(len(city1)):
        compare[f"day_{i + 1}"] = {
            "city_1": city1[f"day_{i + 1}"], 
            "city_2": city2[f"day_{i + 1}"]
            }
    return compare
