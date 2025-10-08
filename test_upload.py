import requests

response = requests.post('http://localhost:8000/compiler/upload', 
                        json={'code': 'var x: number = 10\nprint(x)'})
print('Status:', response.status_code)
print('Response:', response.json())