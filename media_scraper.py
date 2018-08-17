# -*- coding: utf-8 -*-
"""
Created on Thu Aug 1 15:48:39 2018

@author: Abinfinity
"""

# scraping images from news site

from bs4 import BeautifulSoup
import requests
import re

class scraper():
	def scraper(key,address):
		url = requests.get(address).text
		link = BeautifulSoup(url,'lxml')
		if key == "hindustan_times":
			urls = " "
			for article in link.find_all('img'):
				image = article.get('src')
				suf = 'https://www.hindustantimes.com/rf/image_size_960x540'
				if suf in image:
					return image
			
		
		elif key == "ndtv_news":
			for article in link.find_all('img'):
				image = article.get('src')
				if ".jpg" in image or ".jpeg" in image:
					return image
		
		elif key == "india_times":
			for article in link.find_all('img'):
				image = article.get('src')
				if ".jpg" in image or ".jpeg" in image:
					if "/thumb/msid" in image:
						return "https://timesofindia.indiatimes.com"+image
				
		elif key == "india_today":
			lnk = link.find('div', class_= 'stryimg')
			for article in link.find_all('img'):
				image = article.get('src')
				return image
				
		elif key == "india_express":
			lnk = link.find('div', class_= 'article_image_wrap')
			for article in link.find_all('img'):
				image = article.get('src')
				if "900X450" in image:
					return image

		elif key == "livemint":
			lnk = link.find('div', class_= 'lead-image')
			for article in link.find_all('img'):
				image = article.get('src')
				if "621x414" in image:
					return image

		elif key == "b_quint":
			for article in link.find_all('img'):
				image = article.get('src')
				suf = "https://assets.bwbx.io/images/"
				if suf in image:
					return image

		elif key == "ib_times":
			for article in link.find_all('img'):
				image = article.get('src')
				if ".jpg" in image or ".jpeg" in image:
					if "cache-img" in image:
						return image

		elif key == "b_today":
			for article in link.find_all('img'):
				image = article.get('src')
				if ".jpg" in image or ".jpeg" in image:
					return image