import requests
from get_mail import send_mail

key = '32ab022bc7604bdf8f5050c2a9efe3e3'
url = ('https://newsapi.org/v2/everything?q=apple&from=2026-11-22&to=2026-11-22&sortBy=popularity&apiKey'
       '=32ab022bc7604bdf8f5050c2a9efe3e3&language=en')

request = requests.get(url)

content = request.json()

body = ''
for article in content['articles'][:20]:
    if article['title'] and article['description'] is not None:
        body = ( body + article['title']
                + '\n' + article['description']
                + article['url']
                + 3 * '\n')


send_mail(body)
