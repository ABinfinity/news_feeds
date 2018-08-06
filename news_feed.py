import requests
import feedparser
import news_scraper


# url_list = {'hindustan_times':'https://www.hindustantimes.com/rss/topnews/rssfeed.xml','ndtv_news':'http://feeds.feedburner.com/ndtvnews-top-stories','india_times':'https://timesofindia.indiatimes.com/rssfeedstopstories.cms','the_hindu':'https://www.thehindu.com/news/feeder/default.rss','india_today':'https://www.indiatoday.in/rss/1206584'}
url_list = {'hindustan_times':'https://www.hindustantimes.com/rss/topnews/rssfeed.xml'}


for key,value in url_list.items():
	d = feedparser.parse(value)
	# print("key----->"+key)
	# print(len(d['entries']))
	try:
		# for sup in range(len(d['entries'])):
		title = "Title-->"+d['entries'][1]['title']
		
		full_story = "Full story-->"+d['entries'][1]['summary_detail']['value']
		
		link = d['entries'][1]['link']
			

	except Exception as e:
		raise e
	
	paragraph = news_scraper.scraper.scraper(key,link)
	print(title)
	print(full_story)
	print(link)
	print(paragraph)
