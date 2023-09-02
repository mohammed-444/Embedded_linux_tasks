import requests

print ("here is your activities suggestion:")

for i in range(10):

    url = requests.get ("https://www.boredapi.com/api/activity")

    print("- " + url.json()['activity'])


   