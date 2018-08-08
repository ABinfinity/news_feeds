from bs4 import BeautifulSoup
import requests
import re

class scraper():
	def scraper(key,address):
		url = requests.get(address).text
		link = BeautifulSoup(url,'lxml')
		if key == 'hindustan_times':
			article = link.find('div', class_='story-details')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'ndtv_news':
			article = link.find('div', class_='ins_storybody')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'india_times':
			article = link.find('div', class_='Normal').get_text()
			return article
		

		elif key == 'the_hindu':
			article = link.find('div', id = re.compile('^content-body-'))
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'india_today':
			article = link.find('div', class_='description')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'reuters':
			article = link.find('div', class_='StandardArticleBody_body')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'indian_express':
			article = link.find('div', id ='storyContent')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'livemint':
			article = link.find('div', class_='content')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'b_quint':
			article = link.find('div', id =re.compile('^card-'))
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'ib_times':
			article = link.find('div', id ='article_content')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		elif key == 'b_today':
			article = link.find('div', class_='story-right relatedstory')
			story = " "
			for para in article.find_all('p'):
				story = story+str(para.text)
			return story
		

		else:
			return "null"