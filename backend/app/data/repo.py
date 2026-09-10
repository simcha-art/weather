from data.io import read_from_json, write_to_json

def add_city(city: dict):
    try:
        cities = read_from_json()
        cities.append(city)
        write_to_json(cities)
        return True
    except Exception as e:
        print(e)
        return False

def remove_city(city: dict):
    try:
        cities = read_from_json()
        cities.remove(city)
        write_to_json(cities)
        return True
    except ValueError as e: 
        print(e)
        return False

def get_all_cities():
    try:
        return read_from_json()
    except Exception as e:
        print(e)

def get_by_id(id: int):
    try: 
        cities = read_from_json()
        cities_ids = list(map(lambda c: c["id"] ,cities))
        index = cities_ids.index(id)
        return cities[index]
    except Exception as e:
        print(e)


    