import requests
headers = {"some_headers":"123"}
response = requests.post("https://playground.learnqa.ru/api/show_all_headers" , headers = headers)
print(response.text)
print(response.headers)
print(response.json())
