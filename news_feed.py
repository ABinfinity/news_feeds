from bs4 import BeautifulSoup
import requests
import feedparser

d = feedparser.parse('https://www.hindustantimes.com/rss/topnews/rssfeed.xml')
print(d['feed']['title'])
print()
