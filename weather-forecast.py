import requests

city= input("enter the city name : ")
print(city)

print("Displaying weather report for: " + city)
url= 'http://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)