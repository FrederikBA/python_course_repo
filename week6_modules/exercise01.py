import requests

api_key = "6b6abd89d47312e8119ceca1a16ab9a0"

lat = "56.162939"
lon = "10.203921"

data = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?lat=56.162939&lon=10.203921&appid=6b6abd89d47312e8119ceca1a16ab9a0"
)


print(data.content)
