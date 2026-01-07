import requests

api_url="https://api.spacexdata.com/v5/launches/latest"

response=requests.get(url=api_url)

allowed=["links","rocket","success","failures","details","crew","ships","capsules","payloads","launchpad","flight_number"]
m=input("Enter any ( links,rocket,success,failures,details,crew,ships,capsules,payloads,launchpad,flight_number ) -- ")

for i,j in response.json().items():
    if m in allowed and i == m and i!="links":
        print (j)


    elif (m in allowed and i == m) and (i=="links" or i=="crew"):
        for key,value in j.items():        
            print(key, " -- ",value) 
              


