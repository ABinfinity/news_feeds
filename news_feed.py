import requests
import feedparser
import news_scraper


url_list = {'hindustan_times':'https://www.hindustantimes.com/rss/topnews/rssfeed.xml',\
			'ndtv_news':'http://feeds.feedburner.com/ndtvnews-top-stories',\
			'india_times':'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',\
			'the_hindu':'https://www.thehindu.com/news/feeder/default.rss',\
			'india_today':'https://www.indiatoday.in/rss/1206584'}



for key,value in url_list.items():
	d = feedparser.parse(value)
	# print("key----->"+key)
	# print(len(d['entries']))
	try:
		for sup in range(len(d['entries'])):
			title = "Title-->"+d['entries'][sup]['title']
			
			short = "Short-->"+d['entries'][sup]['summary_detail']['value']
			
			link = d['entries'][sup]['link']

			paragraph = news_scraper.scraper.scraper(key,link)
			print(title)
			print(short)
			print("link-->"+link)
			print(paragraph)

	except Exception as e:
		raise e
	
	