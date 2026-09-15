from data.io import read_from_json, write_to_json

def add_city(city: dict, explorer_name: str):
    try:
        cities = read_from_json()
        
        cities.get(explorer_name, []).append(city)
        write_to_json(cities)
        return True
    except Exception as e:
        print(e)
        return False

def remove_city(id: int, explorer_name: str):
    try:
        cities = read_from_json()

        explorer_cities: list = cities.get(explorer_name, [])
        for i in range(len(explorer_cities)):
            city = explorer_cities[i]
            if city["id"] == id:
                explorer_cities.pop(i)
                break

        write_to_json(cities)
        return True
    except ValueError as e: 
        print(e)
        return False

def get_all_cities(explorer_name: str):
    try:
        return read_from_json()[explorer_name]
    except Exception as e:
        print(e)

def get_by_id(id: int, explorer_name: str):
    try: 
        explorer_cities = read_from_json()[explorer_name]
        cities_ids = list(map(lambda c: c["id"] ,explorer_cities))
        index = cities_ids.index(id)
        return explorer_cities[index]
    except Exception as e:
        print(e)


    