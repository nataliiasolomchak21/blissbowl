from django.test import TestCase
from .models import Newsletter

class NewsletterModelTest(TestCase):

    def test_create_newsletter_instance(self):
        """
        Test creating a Newsletter instance and saving it to the database.
        """
        email = 'test@example.com'

        # Create a new Newsletter instance
        newsletter = Newsletter(email=email)

        # Save the instance to the database
        newsletter.save()

        # Retrieve the instance from the database and check its attributes
        saved_newsletter = Newsletter.objects.get(email=email)
        self.assertEqual(saved_newsletter.email, email)

        self.assertEqual(str(saved_newsletter), email)
