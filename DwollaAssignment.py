import requests

# API Key
api = "bc620ead2d18122876f00d05d2993999"

# Base url
base = "http://api.openweathermap.org/data/2.5/weather?"

def test_City():
    # Prompt city (only grab first word inputed)
    city = raw_input("Where are you: ").split(' ', 1)[0]

    # Retrieve weather data
    weather = findTemp(city)

    # Ensure city was retrieved
    assert weather["cod"] != "404", "City not found"

    # Print city temperature
    temp = str(weather["main"]["temp"])
    print(city+" weather:\n" + temp + " degrees Farenheit")

def findTemp(city):
    # Api request url
    url = base + "appid=" + api + "&q=" + city

    # Units in Farenheight
    params = {'units': 'imperial'}

    # Get city data
    response = requests.get(url, params=params)

    # Convert json format into python format
    return response.json()

test_City()
