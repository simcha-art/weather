from fastapi import APIRouter, Query
from typing import Annotated
import requests
import json



router = APIRouter(prefix="/cities", tags=["cities"])

@router.get("/")
def find_city(city: Annotated[str, Query(min_length=2, max_length=20)],
              country: Annotated[str | None, Query( min_length=2, max_length=20)] = None):
    city_to_search = city + f",{country}" if country else city
    res = requests.get(f"https://geocoding-api.open-meteo.com/v1/search", params={"name": city_to_search}).json()
    # print("============================================================")
    # print(res)
    # print("============================================================")
    cities = res.get("results", [])
    # print(cities)

    # print(json.dumps(cities, indent=4))
    return list(map(lambda c: {"id": c["id"], "name":c["name"], "latitude" : c["latitude"], "longitude" :c["longitude"], "timezone": c["timezone"]}, cities))





