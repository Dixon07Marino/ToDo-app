from dotenv import load_dotenv
import requests, os

load_dotenv()

url = 'http://localhost/api/protected'

headers = {
    'Authorization': f'Bearer {os.getenv('TOKEN')}'
}

response = requests.get(url, headers=headers).json()

print(response)