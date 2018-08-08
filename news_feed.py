# -*- coding: utf-8 -*-
"""
Created on Thu Aug 1 15:48:39 2018

@author: Abinfinity
"""

import requests
import feedparser
import news_scraper


url_list = {'hindustan_times':'https://www.hindustantimes.com/rss/topnews/rssfeed.xml',\
			'ndtv_news':'http://feeds.feedburner.com/ndtvnews-top-stories',\
			'india_times':'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',\
			'the_hindu':'https://www.thehindu.com/news/feeder/default.rss',\
			'india_today':'https://www.indiatoday.in/rss/1206584',\
			'reuters':'http://feeds.reuters.com/reuters/INtopNews',\
			'indian_express':'http://www.newindianexpress.com/Nation/rssfeed/?id=170&getXmlFeed=true',\
			'livemint':'https://www.livemint.com/rss/homepage',\
			'b_quint':'https://www.bloombergquint.com/stories.rss',\
			'ib_times':'https://www.ibtimes.co.in/rss/feed',\
			'b_today':'https://www.businesstoday.in/rss/rssstory.jsp?sid=105'}



for key,value in url_list.items():
	d = feedparser.parse(value)
	print("key----->"+key)
	
	try:
		# for sup in range(len(d['entries'])):
		title = "Title-->"+d['entries'][0]['title']
		
		short = "Short-->"+d.entries[0].summary
		
		link = d['entries'][0]['link']

		print(title)
		print(short)
		print("link-->"+link)
		paragraph = news_scraper.scraper.scraper(key,link)
		print("para-->"+paragraph)

	except Exception as e:
		print("None to display")
	print()
	print()
	print()
	
	