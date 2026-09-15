from fastapi import APIRouter, HTTPException, Path
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

Id = Annotated[int, Path(gt=0)]
ExplorerName = Annotated[str, Path(min_length=2)]


router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/{explorer_name}", status_code=201)
def create_new_city(city: City, explorer_name: ExplorerName):
    success = repo.add_city(city.__dict__, explorer_name.lower().strip())
    if success:
        return {"success": success, "msg": "city added"}
    else: 
        raise HTTPException(500, "Internal server error")

@router.delete("/{explorer_name}/{city_id}")
def delete_city(city_id: Id, explorer_name: ExplorerName):
    success = repo.remove_city(city_id, explorer_name.lower().strip())
    if (success):
        return {"success": success, "msg": "city deleted"}
    else: 
        raise HTTPException(404, f"city {city_id} not found")

@router.get("/{explorer_name}")
def get_all_favorites(explorer_name: ExplorerName):
    cities = repo.get_all_cities(explorer_name.lower().strip())
    return cities

@router.get("/{explorer_name}/{city_id}")
def get_city_by_id(explorer_name: ExplorerName, city_id: Id ):
    city = repo.get_by_id(city_id, explorer_name.lower().strip())
    if not city:
        raise HTTPException(404, f"city {city_id} not found")
    else:
         return city

