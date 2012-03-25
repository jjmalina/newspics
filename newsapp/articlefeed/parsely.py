import requests
from django.utils import simplejson as json
from articlefeed.utils import normalize_query


def parsely_querystring(query, amount):
    """
    Constructs a querystring to make an http request to Parse.ly
    Uses a query and amount of results to return
    """
    query = normalize_query(query)
    endpoint = "http://simon.parsely.com:8983/solr/goldindex2/select/"
    api_call = "?wt=json&q=%s&start=0&rows=%i&sort=pub_date+desc" % (query, amount)
    querystring = endpoint + api_call
    return querystring


def retrieve_parsely_articles(topic, amount):
    """
    Retrieves articles from Parse.ly for a particular topic
    """
    querystring = parsely_querystring(topic, amount)
    response = requests.get(querystring)
    if response.status_code == 200:
        response_object = json.loads(response.text)
        articles = response_object['response']['docs']
        return articles
    else:
        return []
