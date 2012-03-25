from celery.task import task, periodic_task
from celery.task import subtask
from celery.schedules import crontab

from articlefeed.models import Topic, Image
from articlefeed.articles import save_article
from articlefeed.parsely import retrieve_parsely_articles
from articlefeed.tumblr import tumblr_tag_request, get_topic_image
from articlefeed.scraper import muckrack_trending_topics


import logging
logger = logging.getLogger(__name__)


@task
def download_trending_topic_articles(trending_topic):
    articles = retrieve_parsely_articles(trending_topic, 10)
    for article in articles:
        saved_article, sampled_topics = save_article(article)
        if sampled_topics:
            download_article_topics(saved_article, sampled_topics)


@task
def download_article_topics(article, topics):
    """
    Gets images for each topic for an article from tumblr
    """
    logger.info("Downloading topics")
    for topic_query in topics:
        tumblr_data = tumblr_tag_request(topic_query)
        if tumblr_data:
            logger.info("Searching tumblr response to term %s" % (topic_query))
            topic_image = get_topic_image(tumblr_data)
            if topic_image:
                logger.info("Saving topic and image")
                saved_topic = Topic.objects.create(name=topic_query)
                image, created = Image.objects.get_or_create(
                    image_url=topic_image['url'],
                    image_height=topic_image['height'],
                    image_width=topic_image['width']
                )
                saved_topic.image = image
                saved_topic.article = article
                saved_topic.save()


@periodic_task(run_every=crontab())
def download_new_articles():
    trending_topics = muckrack_trending_topics()
    logger.info("Retrieved trending topics from Muck Rack " + repr(trending_topics))
    logger.info("Downloading articles for each trending topic")
    for trending_topic in trending_topics:
        download_trending_topic_articles(trending_topic)
    

