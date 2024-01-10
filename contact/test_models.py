from django.test import TestCase
from .models import ContactMessage

class ContactMessageModelTest(TestCase):

    def test_create_contact_message(self):
        """
        Test creating a ContactMessage instance.
        """
        contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            message='Test message'
        )

        self.assertEqual(contact_message.name, 'John Doe')
        self.assertEqual(contact_message.email, 'john@example.com')
        self.assertEqual(contact_message.message, 'Test message')

    def test_contact_message_str_method(self):
        """
        Test the __str__ method of the ContactMessage model.
        """
        contact_message = ContactMessage.objects.create(
            name='Jane Doe',
            email='jane@example.com',
            message='Another test message'
        )

        self.assertEqual(str(contact_message), 'Jane Doe')
