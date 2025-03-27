import requests
from datetime import datetime


response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()


print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

position = (longitude, latitude)
parameters = {
    "lat" : "47.143467",
    "lng" : "23.878899",
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now().hour









