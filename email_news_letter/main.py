import requests
from get_mail import send_mail

key = '32ab022bc7604bdf8f5050c2a9efe3e3'
url = ('https://newsapi.org/v2/everything?q=tesla&from=2026-10-19&sortBy=publishedAt&apiKey'
       '=32ab022bc7604bdf8f5050c2a9efe3e3')

request = requests.get(url)

content = request.json()

body = ''
for article in content['articles']:
    body = body + article['title'] + '/n' + article['description'] + 3 * '/n'

body = body.encode('utf-8')
send_mail(body)
