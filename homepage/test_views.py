from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('homepage')

    def test_index_view(self):
        """
        Test GET request to the index view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')
