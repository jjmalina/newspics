from django.db import models


class Image(models.Model):
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
    url = models.URLField(
        verify_exists=False,
        max_length=255,
        unique=True,
        help_text='The full, canonical, non-shortened URL for the article.'
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    author_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Author name as given by an external API."
    )
    content = models.TextField(
        blank=True,
        null=True,
        help_text="Original content for the article"
    )
    pub_date = models.DateTimeField()
    date_downloaded = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(Image, through='Topic', related_name='articles')


class Topic(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    article = models.ForeignKey(Article, related_name='topics')
    image = models.ForeignKey(Image, related_name='topics')
    date_downloaded = models.DateTimeField(auto_now_add=True)
