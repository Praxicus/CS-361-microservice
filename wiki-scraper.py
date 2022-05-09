import requests
from bs4 import BeautifulSoup
import sys

def scrape(link):
	response = requests.get(url = link,)

	soup = BeautifulSoup(response.content, 'html.parser')
	list(soup.children)

	info = soup.find(id='mw-content-text').find_all('p')

	f = open('wiki.txt', 'w')
	for para in info:
		f.write(para.get_text())
		f.write('\n')


page = sys.argv[1]
page = page.replace(' ', '_')
page.lower()

link = ('https://en.wikipedia.org/wiki/' + page)

print(link + '\n')

scrape(link)
