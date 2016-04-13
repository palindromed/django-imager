# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory
from imager_profile.models import ImagerProfile

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    # photography_type = 'N'
    username = 'john'
    # email = factory.LazyAttribute(
    #     lambda x: "{}@example.com".format(x.username))


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build(username='sarah')
        self.user.set_password('secret')
        self.user.camera = 'nikon'
        # self.user = UserFactory()
        self.user2 = UserFactory.build(username='scott')
        self.user2.set_password('1234')

    def tearDown(self):
        pass


    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(ImagerProfile.objects.count() == 0)
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)


    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)


    def test_instance(self):
        self.user.save()
        self.assertIsInstance(self.user.profile, ImagerProfile)

    def test_is_active(self):
        self.user.save()
        assert self.user.profile.is_active

    def test_location(self):
        self.user.save()
        assert self.user.profile.location == ''

    def test_friends(self):
        self.user.save()
        # self.user2.save()
        # self.user.profile.friends.add(self.user2)
        # profile = ImagerProfile.objects.get(user=self.user)
        assert self.user.profile.friends
        # self.user.save()

        # assert self.user.friends

    def test_camera(self):
        self.user.save()
        assert self.user.profile.camera == ''

    def test_photograpy_type(self):
        self.user.save()

        assert self.user.profile.photography_type

