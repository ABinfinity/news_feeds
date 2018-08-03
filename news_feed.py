from bs4 import BeautifulSoup
import requests
import feedparser

d = feedparser.parse('https://www.hindustantimes.com/rss/topnews/rssfeed.xml')
print(d['entries'][1]['title'])
# print()
# print(d['entries'][1]['title_detail']['value'])
print()
print(d['entries'][1]['summary'])
# print()
# print(d['entries'][1]['summary_detail']['value'])
print()
print(d['entries'][1]['media_content'][0]['url'])
print()
# try:
# 	for sup in range(len(d['entries'])):
# 		print("Title-->"+d['entries'][sup]['title'])
# 		print()
# 		print("Full story-->"+d['entries'][sup]['summary_detail']['value'])
# 		print()
# 		print("link-->"+d['entries'][sup]['link'])
# 		print()

# except Exception as e:
# 	raise e
