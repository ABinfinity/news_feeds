from bs4 import BeautifulSoup
import requests
import re

class scraper():
	def scraper(key,address):
		url = requests.get(address).text
		link = BeautifulSoup(url,'lxml')
		if key == 'hindustan_times':
			article = link.find('div', class_='story-details').get_text()
			return article
		elif key == 'ndtv_news':
			article = link.find('div', class_='ins_storybody').get_text()
			return article
		elif key == 'india_times':
			article = link.find('div', class_='Normal').get_text()
			return article
		elif key == 'the_hindu':
			article = link.find('div', id = re.compile('^content-body-')).get_text()
			return article
		elif key == 'india_today':
			article = link.find('div', class_='description').get_text()
			return article
		elif key == 'reuters':
			article = link.find('div', class_='StandardArticleBody_body').get_text()
			return article
		elif key == 'indian_express':
			article = link.find('div', id ='storyContent').get_text()
			return article
		elif key == 'livemint':
			article = link.find('div', class_='content').get_text()
			return article
		elif key == 'b_quint':
			article = link.find('div', id =re.compile('^card-')).get_text()
			return article
		elif key == 'ib_times':
			article = link.find('div', id ='article_content').get_text()
			return article
		elif key == 'b_today':
			article = link.find('div', class_='story-right relatedstory').get_text()
			return article
		else:
			return "null"