import requests
import json

def get_swapi_data(url):
    response = requests.get(url)
    return response.json()

def get_millennium_falcon_info():
    falcon_url = "https://swapi.dev/api/starships/10/"
    falcon_data = get_swapi_data(falcon_url)

    pilots_info = []
    for pilot_url in falcon_data["pilots"]:
        pilot_data = get_swapi_data(pilot_url)
        homeworld_data = get_swapi_data(pilot_data["homeworld"])

        pilot_info = {
            "name": pilot_data["name"],
            "height": pilot_data["height"],
            "mass": pilot_data["mass"],
            "homeworld": homeworld_data["name"],
            "homeworld_url": pilot_data["homeworld"],
        }

        pilots_info.append(pilot_info)

    millennium_falcon_info = {
        "max_atmosphering_speed": falcon_data["max_atmosphering_speed"],
        "starship_class": falcon_data["starship_class"],
        "pilots": pilots_info,
    }

    return millennium_falcon_info

def main():
    falcon_info = get_millennium_falcon_info()
    formatted_info = json.dumps(falcon_info, indent=2, ensure_ascii=False)
    print(formatted_info)

if __name__ == "__main__":
    main()
