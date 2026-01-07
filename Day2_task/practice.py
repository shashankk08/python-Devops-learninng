import requests

pj_url="https://official-joke-api.appspot.com/random_joke"
dad_url="https://icanhazdadjoke.com/"

def get_joke(url_type,mood):
    headers = {"Accept": "application/json"}
    response=requests.get(url=url_type,headers=headers)
    
    if mood=="dad":
        return response.json()["joke"]
    else:
        return response.json()["setup"]+response.json()["punchline"]


user=input("select mood , eg- dad or pj ")

if user=="dad":
    url_type=dad_url

else:
    url_type=pj_url
    

print(get_joke(url_type,user))



