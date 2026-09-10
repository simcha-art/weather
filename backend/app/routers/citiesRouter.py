from fastapi import APIRouter
import requests
import json

router = APIRouter(prefix="/cities", tags=["cities"])

@router.get("/")
def find_city(city: str, country: str = None):
    city_to_search = city + f",{country}" if country else city
    res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search", params={"name": city_to_search})
    print(res)
    cities = res.json()["results"]
    # print(cities)
    print(json.dumps(cities, indent=4))
    return list(map(lambda c: {"id": c["id"], "name":c["name"], "latitude" : c["latitude"], "longitude" :c["longitude"], "timezone": c["timezone"]}, cities))






