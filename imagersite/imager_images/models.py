from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


PUBLISHED_CHOICES = (
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
)


@python_2_unicode_compatible
class Photo(models.Model):
    """Create a photo instance belonging to one user that can be in many albums."""

    file = models.ImageField(upload_to='images/%Y-%m-%d')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        related_name='photos'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)

    published = models.CharField(max_length=255,
                                 choices=PUBLISHED_CHOICES,
                                 default='public')

    def __str__(self):
        """Return photo title."""
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    """Create an album that belongs to one user and can contain many photos."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='albums',
        null=False
    )
    album_photos = models.ManyToManyField(
        Photo,
        related_name='albums',
    )
    cover = models.ForeignKey(
        Photo,
        related_name='cover_image'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.CharField(max_length=255,
                                 choices=PUBLISHED_CHOICES,
                                 default='public')

    def __str__(self):
        """Return album title."""
        return self.title
