from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class HomeViewTest(TestCase):

    def setUp(self):
        self.url = reverse('home')

    def test_get_success(self):
        c = Client()
        response = c.get(self.url)
        self.assertEqual(response.status_code, 200)