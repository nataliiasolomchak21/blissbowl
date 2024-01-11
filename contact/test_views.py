from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm
from .models import ContactMessage


class ContactUsViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact_us')

    def test_contact_us_view_get(self):
        """
        Test GET request to the contact_us view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_us_view_post_valid_form(self):
        """
        Test POST request to the contact_us view with a valid form.
        """
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Test message'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact_us'))
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().name, 'John Doe')

    def test_contact_us_view_post_invalid_form(self):
        """
        Test POST request to the contact_us view with an invalid form.
        """
        data = {}  # Invalid data with missing required fields
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertContains(response, 'Form submission failed.')
