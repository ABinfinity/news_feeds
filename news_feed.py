from bs4 import BeautifulSoup
import requests
import feedparser

d = feedparser.parse('https://www.hindustantimes.com/rss/topnews/rssfeed.xml')
# print(d['feed']['subtitle'])
try:
	for sup in range(len(d['entries'])):
		print("Title-->"+d['entries'][sup]['title'])
		print()
		print("Full story-->"+d['entries'][sup]['summary_detail']['value'])
		print()
		print("link-->"+d['entries'][sup]['link'])
		print()

except Exception as e:
	raise e
