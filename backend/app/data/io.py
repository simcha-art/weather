import json
FILE_PATH = "./favorites.json"


def write_to_json(data: list[dicts]):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e: 
        print(e)


def read_from_json():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except FileNotFoundError:
        write_to_json([])
        return []

    except PermissionError:
        print(f"permission to file {FILE_PATH} denied")
    except Exception as e:
        print(e)