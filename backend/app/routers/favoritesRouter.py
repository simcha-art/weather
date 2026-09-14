from fastapi import APIRouter, HTTPException, Query
from data import repo
from pydantic import BaseModel, Field
from typing import Annotated

from .weaterRouter import Longitude, Latitude

class City(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=20)
    latitude: Latitude
    longitude: Longitude
    timezone: str = Field(min_length=2)

Id = Annotated[int, Query(gt=0)]


router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/new", status_code=201)
def create_new_city(city: City):
    success = repo.add_city(city)
    if success:
        return {"success": success, "msg": "city added"}
    else: 
        raise HTTPException(500, "Internal server error")

@router.delete("/delete")
def delete_city(city: City):
    success = repo.remove_city(city)
    if (success):
        return {"success": success, "msg": "city deleted"}
    else: 
        raise HTTPException(404, f"city {city["id"]} not found")

@router.get("")
def get_all_favorites():
    cities = repo.get_all_cities()
    return cities

@router.get("/:id")
def get_city_by_id(id: Id):
    city = repo.get_by_id(id)
    if not city:
        raise HTTPException(404, f"city {id} not found")
    else:
         return city

