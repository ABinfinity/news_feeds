# -*- coding: utf-8 -*-
"""
Created on Thu Aug 1 15:48:39 2018

@author: Abinfinity
"""

import requests
import feedparser
import news_scraper as ns # scapre paragraph
import media_scraper as ms # scrape images
import para_summary as ps # gives summary
from flask import Flask,jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class feedup(Resource):
	def post(self):
		return 200


	def get(self):
		#list of rss news source
		url_list = {'hindustan_times':'https://www.hindustantimes.com/rss/topnews/rssfeed.xml',\
		            # 'ndtv_news':'http://feeds.feedburner.com/ndtvnews-top-stories',\
		           #  'india_times':'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',\
		           #  #'the_hindu':'https://www.thehindu.com/news/feeder/default.rss',\
		           #  'india_today':'https://www.indiatoday.in/rss/1206584',\
		           # # 'reuters':'http://feeds.reuters.com/reuters/INtopNews',\
		           #  'indian_express':'http://www.newindianexpress.com/Nation/rssfeed/?id=170&getXmlFeed=true',\
		           #  'livemint':'https://www.livemint.com/rss/homepage',\
		           #  'b_quint':'https://www.bloombergquint.com/stories.rss',\
		           #  'ib_times':'https://www.ibtimes.co.in/rss/feed',\
		            # 'b_today':'https://www.businesstoday.in/rss/rssstory.jsp?sid=105'
		            }

		news = dict()
		for key,value in url_list.items():
			d = feedparser.parse(value)
			print("source----->"+key)
			# print(d['entries'][0])
			page = []
			try:
				for sup in range(len(d['entries'])):
					title = d['entries'][sup]['title']
					link = d['entries'][sup]['link']
					# paragraph = ns.scraper.scraper(key,link)
					media = ms.scraper.scraper(key,link)
					paragraph = ps.para.summ(link)
					data = {"title": title, "link": link, "media_link" : media, "summary": paragraph}
					page.append(data)
			
			except Exception as e:
				print("None to display")
			
			news[key] = page


		
		return jsonify(news),200

api.add_resource(feedup, '/print')

if __name__ == '__main__':
	app.run(debug = True)

	
	