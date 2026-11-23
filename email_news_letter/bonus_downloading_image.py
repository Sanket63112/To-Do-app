#downloading image from browser using url
import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/<x>/<xy>/SEN_TENZ_2023.jpg'

response = requests.get(url)

with open('image.jpg', 'wb') as file:
    file.write(response.content)
