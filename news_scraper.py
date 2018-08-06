from bs4 import BeautifulSoup
import requests

class scraper():
	def scraper(key,address):
		url = requests.get(address).text
		link = BeautifulSoup(url,'lxml')
		article = link.find('div', class_='story-details').text
		return article