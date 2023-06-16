import requests
response=requests.get("https://www.codewithharry.com")
print(response.text)
url="https://jsonplaceholder.typicode.com/posts"
response=requests.post(url,headers=headers,json=data)
print(response.text)