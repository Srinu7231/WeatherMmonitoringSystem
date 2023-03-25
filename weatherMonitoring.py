import requests

from twilio.rest import Clien
# goto Twilio web site and create your account and you will get these ids
account_sid = 'your accout SID'
auth_token = 'Your auth token'

client = Client(account_sid, auth_token)


api_key = 'Your weather api key'
lat = 18.111240
lng = 83.397392
parameters = {
    'lat': lat,
    "lon": lng,
    "appid": api_key,
    'exclude': 'daily,minutely,current'
}
url = 'https://api.openweathermap.org/data/2.5/onecall'   #goto this link and create your login and create your api key
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
            from_='TWILIO_NUMBER',
            to='RECEIVER_NUMBER'
        )
        print(message.status)
        break
    hrs += 1
print(weather)



