import requests

from twilio.rest import Client
# account_sid = 'AC708aced84c44441e7e69e61e62ed9c6f'
# ac = os.environ[account_sid]
# auth_token = 'c4b990c64c333ecc3e6aaf90f8c5047d'
# at = os.environ[auth_token]
account_sid = 'AC708aced84c44441e7e69e61e62ed9c6f'
auth_token = 'c4b990c64c333ecc3e6aaf90f8c5047d'

client = Client(account_sid, auth_token)


api_key = '1d15d3b3e1eebdf5b0950f5de36c1bb5'
lat = 18.111240
lng = 83.397392
parameters = {
    'lat': lat,
    "lon": lng,
    "appid": api_key,
    'exclude': 'daily,minutely,current'
}
url = 'https://api.openweathermap.org/data/2.5/onecall'
response = requests.get(url=url, params=parameters)
print(response)
data = response.json()
print(data)
twhrs = data['hourly'][0:12]
weather = []
hrs = 0
for i in twhrs:
     # print(i)
    id = i['weather'][0]['id']
    weather.append(id)
    if id < 700:
        message = client.messages.create(
            body=f"Today it's gonna rain in {hrs}hrs !! Weather Condition:{i['weather'][0]['description']}\n"
                 f" Bring your ☂️ ☂️ ☂️ Umbrilla ☂️ ☂️ ☂️  with you !!",
            from_='+18317776116',
            to='+917286874152'
        )
        print(message.status)
        break
    hrs += 1
print(weather)



