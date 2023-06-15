import requests
import webbrowser


def display_bing_map(latitude, longitude, zoom, locations):
    api_key = "AlcfAk5eTMkn5lHe9akGI64L4JSaIrrFlTyYlt8Ei2HQE7PPSFeJc5R_BVSDmIRC"
    locations_param = "|".join(locations)
    url = f"https://www.bing.com/maps/embed?h=800&w=1000&cp={latitude}~{longitude}&lvl={zoom}&typ=d&sty=r&src=SHELL&FORM=MBEDV8&pushpins={locations_param}"
    webbrowser.open(url)

def get_nearby_hospitals(latitude, longitude, radius):
    api_key = "<YOUR-API-KEY>"
    url = f"https://atlas.microsoft.com/search/poi/json?api-version=1.0&query=hospitals&subscription-key={api_key}&lat={latitude}&lon={longitude}&radius={radius}"
    response = requests.get(url)
    data = response.json()
    hospitals = []
    print(data)

    for result in data['results']:
        hospital = {
            'name': result['poi']['name'],
            'latitude': result['position']['lat'],
            'longitude': result['position']['lon'],
            'distance': result['dist']
        }
        print(hospital)
        hospitals.append(hospital)
    return hospitals


# Provide the latitude, longitude, and zoom level
latitude = 12.9291089
longitude = 80.1598282
zoom = 14
radius = 1000

hospitals = get_nearby_hospitals(latitude, longitude, radius)

locations = []

print(hospitals)

for hospital in hospitals:
    name = hospital['name']
    latitude = hospital['latitude']
    longitude = hospital['longitude']
    locations.append(f"{latitude},{longitude}")
    print(f"Hospital Name: {name}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print()

display_bing_map(latitude, longitude, zoom, locations)
