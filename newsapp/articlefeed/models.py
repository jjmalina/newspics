from django.db import models
from batch_select.models import BatchManager
import jsonfield


class Image(models.Model):
    objects = BatchManager()
    image_url = models.URLField(
        verify_exists=False,
        max_length=255,
        unique=True,
        help_text='The full, canonical, non-shortened URL for the image.'
    )
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    date_downloaded = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    objects = BatchManager()
    url = models.URLField(
        verify_exists=False,
        max_length=255,
        unique=True,
        help_text='The full, canonical, non-shortened URL for the article.'
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=40, blank=True, null=True)
    author_name = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        help_text="Author name as given by an external API."
    )
    content = models.TextField(
        blank=True,
        null=True,
        help_text="Original content for the article"
    )
    pub_date = models.DateTimeField(blank=True, null=True)
    date_downloaded = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image, through='Topic', related_name='articles')
    parsely_topics = jsonfield.JSONField(blank=True,null=True)
    has_topics_and_image = models.BooleanField(default=False)


class Topic(models.Model):
    objects = BatchManager()
    name = models.CharField(max_length=40, blank=True, null=True)
    article = models.ForeignKey(Article, null=True, related_name='topics')
    image = models.ForeignKey(Image, null=True, related_name='topics')
    date_downloaded = models.DateTimeField(auto_now_add=True)
