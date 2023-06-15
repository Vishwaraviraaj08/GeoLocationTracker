import requests
import webbrowser

def display_bing_map(latitude, longitude, zoom, locations):
    api_key = "AlcfAk5eTMkn5lHe9akGI64L4JSaIrrFlTyYlt8Ei2HQE7PPSFeJc5R_BVSDmIRC"
    locations_param = "|".join(locations)
    url = f"https://www.bing.com/maps/embed?h=800&w=1000&cp={latitude}~{longitude}&lvl={zoom}&typ=d&sty=r&src=SHELL&FORM=MBEDV8&pushpins={locations_param}"
    webbrowser.open(url)

def get_nearby_hospitals(latitude, longitude, radius):
    api_key = "AlcfAk5eTMkn5lHe9akGI64L4JSaIrrFlTyYlt8Ei2HQE7PPSFeJc5R_BVSDmIRC"
    url = f"https://dev.virtualearth.net/REST/v1/LocalSearch/?query=hospital&userCircularMapView={latitude},{longitude},{radius}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    hospitals = []
    print(data)

    for result in data['resourceSets'][0]['resources']:
        hospital = {
            'name': result['name'],
            'latitude': result['point']['coordinates'][0],
            'longitude': result['point']['coordinates'][1]
        }
        print(hospital)
        hospitals.append(hospital)

    return hospitals

# Provide the latitude, longitude, and zoom level
latitude = 37.7749
longitude = -122.4194
zoom = 12
radius = 10

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
