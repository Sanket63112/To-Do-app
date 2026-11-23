import requests
import streamlit as st
import re
from html import unescape


def clean_html(text: str) -> str:
    text = re.sub(r'<br\s*/?>', '\n', text)  # keep line breaks
    text = re.sub(r'</p>', '\n\n', text)
    text = re.sub(r'<[^>]+>', '', text)  # remove all remaining tags
    text = unescape(text)  # &amp; &quot; &#39; etc.
    return text.strip()


api_key = 'WK96rpFrfTTtGr6GPzBPfm7WFbtLgchBqJCrCCnb'
url = f'https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key={api_key}'

response = requests.get(url)
data = response.json()
print(data)

title = data[0]['title']
image_url = data[0]['hdurl']
description = clean_html(data[0]['explanation'])

image = 'img.jpg'
headers = {"User-Agent": "my-newsletter/1.0"}  # NASA blocks default UA sometimes
image_response = requests.get(image_url, headers=headers)
with open(image, 'wb') as file:
    file.write(image_response.content)

    st.title(title)
    st.image(image)
    st.write(description)
