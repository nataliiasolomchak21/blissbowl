from django.test import TestCase, Client
from django.urls import reverse
from .models import Newsletter

class NewsletterFormTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('newsletter')

    def test_newsletter_form_valid_data(self):
        """
        Test submitting the newsletter form with valid data.
        """
        valid_data = {
            'email': 'test@example.com',
        }
        response = self.client.post(self.url, data=valid_data)
        self.assertEqual(response.status_code, 302)  # 302 indicates a successful form submission

        self.assertTrue(Newsletter.objects.filter(email=valid_data['email']).exists())

    def test_newsletter_form_invalid_data(self):
        """
        Test submitting the newsletter form with invalid data.
        """
        invalid_data = {
            'email': 'invalid-email',  # Invalid email format
        }
        response = self.client.post(self.url, data=invalid_data)
        self.assertEqual(response.status_code, 200)  # 200 indicates a failed form submission

        self.assertFalse(Newsletter.objects.filter(email=invalid_data['email']).exists())
