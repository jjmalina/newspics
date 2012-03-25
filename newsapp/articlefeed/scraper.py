import requests
from pyquery import PyQuery as pq

def muckrack_trending_topics():
	"""
	Scrapes muckrack.com for trending topics
	"""
	response = requests.get('http://muckrack.com')
	html = response.text
	dom = pq(html)
	trending_list = dom('.trending')
	return [topic.text for topic in trending_list]
