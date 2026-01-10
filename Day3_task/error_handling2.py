import requests

api_url="https://api.spacexdata.com/v5/launches/latest"

def call_api():
    response=requests.get(url=api_url)
    return response.json()

api_output=call_api()



try:
    user_input=int(input("Enter any numeric no. for option check - "))
    print(list(api_output.keys()))
    
    user_input2=input("Enter any SpaceX unit , which you want to check ")
    
    if user_input2=="links":
        print(api_output["links"])
    elif user_input2=="crew":
        print(api_output["crew"])
    elif user_input2=="cores":
        print(api_output["cores"])
    else:
        print(api_output[user_input2])

except Exception as e:
    print("Error",e)  