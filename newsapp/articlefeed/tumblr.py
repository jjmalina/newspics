import requests
import settings
from django.utils import simplejson as json
from operator import itemgetter

from articlefeed.utils import normalize_query

tumblr_key = settings.TUMBLR_KEY


def tumblr_tag_querystring(query):
    """
    Constructs a URL for a call to Tumblr's API
    """
    query = normalize_query(query)
    endpoint = 'http://api.tumblr.com/v2/'
    api_call = 'tagged?tag=%s&api_key=%s' % (query, tumblr_key)
    return endpoint + api_call


def tumblr_tag_request(tag_query):
    """
    Makes an API request to Tumblr to get images back from a tag request
    """
    querystring = tumblr_tag_querystring(tag_query)
    response = requests.get(querystring)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def get_topic_image(tumblr_data):
    """
    Returns the most recent image and it's size from the tumblr response
    """
    photo_post = None
    sort = False
    sorted_posts = []
    posts = tumblr_data['response']
    try:
        sorted_posts = sorted(posts, key=itemgetter('note_count'))
        sort = True
    except KeyError:
        pass

    if sort:
        posts = reversed(sorted_posts)  
        
    for post in posts:
        if post['type'] == 'photo':
            photo_post = post
            break
    if not photo_post:
        return None
    else:
        post_photo = photo_post['photos'][0]
        return post_photo['alt_sizes'][1]

