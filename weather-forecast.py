import requests

city= input("enter the city name : ")
print(city)

print("Displaying Weather Report For: " + city)
url= 'http://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)
