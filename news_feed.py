# -*- coding: utf-8 -*-
"""
Created on Thu Aug 1 15:48:39 2018

@author: Abinfinity
"""

import requests
import feedparser
import news_scraper as ns
import media_scraper as ms
import para_summary as ps
import json


url_list = {'hindustan_times':'https://www.hindustantimes.com/rss/topnews/rssfeed.xml',\
            'ndtv_news':'http://feeds.feedburner.com/ndtvnews-top-stories',\
            'india_times':'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',\
            #'the_hindu':'https://www.thehindu.com/news/feeder/default.rss',\
            'india_today':'https://www.indiatoday.in/rss/1206584',\
           # 'reuters':'http://feeds.reuters.com/reuters/INtopNews',\
            'indian_express':'http://www.newindianexpress.com/Nation/rssfeed/?id=170&getXmlFeed=true',\
            'livemint':'https://www.livemint.com/rss/homepage',\
            'b_quint':'https://www.bloombergquint.com/stories.rss',\
            'ib_times':'https://www.ibtimes.co.in/rss/feed',\
            'b_today':'https://www.businesstoday.in/rss/rssstory.jsp?sid=105'}





for key,value in url_list.items():
	d = feedparser.parse(value)
	print("key----->"+key)
	# print(d['entries'][0])
	# print()
	
	try:
		for sup in range(len(d['entries'])):
			title = d['entries'][sup]['title']
			link = d['entries'][sup]['link']
			# paragraph = ns.scraper.scraper(key,link)
			media = ms.scraper.scraper(key,link)
			paragraph = ps.summ(link)
			print(title)
			# print(link)
			# print(paragraph)
			print(media)

					
			

	except Exception as e:
		print("None to display")
	




















	
	