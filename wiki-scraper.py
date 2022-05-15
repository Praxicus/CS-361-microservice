import requests
from bs4 import BeautifulSoup
from flask import Flask, request, json

app = Flask(__name__)

@app.get('/scrape')
def scrape():
	page = request.args.get('page')
	page = page.replace(' ', '_')
	page.lower()
	response = requests.get(url = ('https://en.wikipedia.org/wiki/' + page))

	soup = BeautifulSoup(response.content, 'html.parser')
	list(soup.children)

	info = soup.find(id='mw-content-text').find_all('p')
	
	article = ''

	for para in info:
		article = article + para.get_text()

	wiki = {
		'page': page.lower(),
		'link': 'https://en.wikipedia.org/wiki/' + page,
		'article': article
	}

	# f = open('wiki.txt', 'w', encoding="utf-8")
	# for para in info:
	# 	f.write(para.get_text())
	# 	f.write('\n')

	return json.dumps(wiki)
		
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=3000, debug=True)
