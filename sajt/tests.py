from django.test import TestCase
from sajt.models import *


class SubscriberTest(TestCase):

	def setUp(self):
		Subscriber.objects.create(name="Petar Petrovic", email="petar.petrovic@nomail.com", is_active=True)


	def test_subscriber(self):
		subscriber = Subscriber.objects.get(email="petar.petrovic@nomail.com")

