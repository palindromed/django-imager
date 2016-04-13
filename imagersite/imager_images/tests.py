# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from imager_images.models import Photo, Album
from imager_profile.tests import UserFactory

# Create your tests here.


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
    file = factory.django.ImageField(color='red')


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album


class ImageTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory.create(username='sarah')
        self.user.set_password('secret')
        self.user.save()

        self.photo = PhotoFactory.create(user=self.user)
        self.album = AlbumFactory.create(user=self.user, cover=self.photo)


    def test_image_in_album(self):
        self.photo.albums.add(self.album)
        self.photo.save()
        assert self.photo.albums.all()

    def test_image_has_user(self):
        assert self.photo.user is self.user

    def test_user_assoc_with_photo(self):
        assert self.photo.user.username == 'sarah'

    def test_user_has_image(self):
        self.assertEqual(self.photo.user.username, self.user.username)

    def test_title(self):
        assert self.photo.title == ''


    def test_description(self):
        assert self.photo.description == ''


    def test_settings(self):
        assert self.photo.published == 'public'

    def test_album_add_and_remove(self):
        # image = PhotoFactory()
        # album = AlbumFactory()
        self.photo.albums.add(self.album)
        self.album.cover = self.photo
        self.album.save()
        assert self.album.cover == self.photo
        assert self.album in Album.objects.all()
