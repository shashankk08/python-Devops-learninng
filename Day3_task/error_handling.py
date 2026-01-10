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
    
    for i,j in api_output.items():
        if user_input2==i:
            print(j)

except Exception as e:
    print("Error",e)    



# for i,j in api_output.items():
#     print(i," -- ",j)
#     print("===========================================")              


