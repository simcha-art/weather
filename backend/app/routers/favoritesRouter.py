from fastapi import APIRouter, HTTPException
from data import repo

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/new", status_code=201)
def create_new_city(city: dict):
    success = repo.add_city(city)
    if success:
        return {"success": success, "msg": "city added"}
    else: 
        raise HTTPException(500, "Internal server error")

@router.delete("/delete")
def delete_city(city: dict):
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
def get_city_by_id(id: int):
    city = repo.get_by_id(id)
    if not city:
        raise HTTPException(404, f"city {id} not found")
    else:
         return city

