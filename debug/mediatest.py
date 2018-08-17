# -*- coding: utf-8 -*-
"""
Created on Thu Aug 1 15:48:39 2018

@author: Abinfinity
"""

# for debugging media files

from bs4 import BeautifulSoup
import requests
import re
import feedparser

def passed():
	address = "https://www.thehindu.com/news/feeder/default.rss"
	feed = feedparser.parse(address)
	for sup in range(len(feed['entries'])):
		link = feed['entries'][sup]['link']
		title = feed['entries'][sup]['title']
		print(title)
		print(link)
		imagescar(link)

def imagescar(address):
	url = requests.get(address).text
	link = BeautifulSoup(url,'lxml')
	urls = " "
	lnk = link.find('div', class_ = 'image-container picture')
	# article = lnk.find('img')
	print(lnk)
	# image = article.get('src')
		# if ".jpg" in image or ".jpeg" in image:
			# if "cache-img" in image:
			# return image
	
	# print(image)
	# print()


if __name__ == '__main__':
	passed()