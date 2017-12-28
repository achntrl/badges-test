from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from datetime import timedelta

from .models import Star, Collector, Pioneer, PowerUser
from models3d.models import Model


class BadgeTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='password',
            date_joined=timezone.now() - timedelta(days=365),
        )
        self.user_without_badges = User.objects.create_user(
            username='without_badge',
            password='password',
            date_joined=timezone.now(),
        )

    def test_star(self):
        model = Model.objects.create(user=self.user, name='cube')

        for _ in range(100):
            self.client.get('/models/' + model.name)

        self.assertTrue(Star.objects.filter(user=self.user))
        self.assertFalse(Star.objects.filter(user=self.user_without_badges))

    def test_collector(self):
        self.client.login(username=self.user.username, password='password')

        for _ in range(5):
            with open('data/tests/triangle.obj') as fd:
                self.client.post('/models', data={'file': fd})

        self.assertTrue(Collector.objects.filter(user=self.user))
        self.assertFalse(Collector.objects.filter(user=self.user_without_badges))

    def test_pioneer(self):
        self.client.login(username=self.user.username, password='password')
        self.assertTrue(Pioneer.objects.filter(user=self.user))
        self.assertFalse(Pioneer.objects.filter(user=self.user_without_badges))

    def test_power_user(self):
        self.client.login(username=self.user.username, password='password')
        with open('data/tests/big_model.obj') as fd:
                self.client.post('/models', data={'file': fd})

        self.assertTrue(PowerUser.objects.filter(user=self.user))
        self.assertFalse(PowerUser.objects.filter(user=self.user_without_badges))
