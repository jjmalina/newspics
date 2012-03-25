import random
from datetime import datetime
from articlefeed.models import Article

topics_per_article = 5

def randomize_indices(sample_size, items_returned):
    """
    For an integer range, returns an arbitrary amount of unique integers in a list
    """
    if items_returned > sample_size:
        return [0,]
    elif items_returned == sample_size:
        return [number for number in range(items_returned)]
    else:
        items = [number for number in range(items_returned)]
        random.shuffle(items)
        return items[:items_returned]


def sample_topics(topics):
    sample = randomize_indices(len(topics), topics_per_article)
    sampled_topics = []
    for index in sample:
        sampled_topics.append(topics[index])
    return sampled_topics

def save_article(article_data):
    """
    Creates a new article if it doesn't already exist in the database
    """
    url = article_data['url']
    article, created = Article.objects.get_or_create(url=url)
    if created:
        article.title = article_data['title']
        article.publisher = article_data['publisher']
        article.author = article_data['author']
        article.content = article_data['full_content']
        article.parsely_topics = article_data['topics']
        article.pub_date = datetime.strptime(article_data['pub_date'], '%Y-%m-%dT%H:%M:%SZ')
        article.save()
        sampled_topics = sample_topics(article_data['topics'])
        return article, sampled_topics
    else:
        return article, None


