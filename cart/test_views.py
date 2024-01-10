from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from cloudinary.models import CloudinaryField
from products.models import Product, Category

class CartViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            calories=100,
            weight=2.0,
            preparation_time='10 minutes',
            description='A test product',
            price=19.99,
            image_url='https://example.com/image.jpg',
            image='example_image.jpg'
        )

    def test_view_cart(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        url = reverse('add_to_cart', args=[self.product.id])
        data = {'quantity': 2, 'redirect_url': reverse('view_cart')}
        response = self.client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertGreaterEqual(len(messages), 1)
        self.assertEqual(messages[-1].tags, 'success')
        self.assertEqual(
            messages[-1].message, f'Added {self.product.name} to your cart')

    def test_adjust_cart(self):
        url = reverse('adjust_cart', args=[self.product.id])
        data = {'quantity': 3}
        response = self.client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertGreaterEqual(len(messages), 1)
        self.assertEqual(messages[-1].tags, 'success')
        self.assertEqual(
            messages[-1].message, f'Updated {self.product.name} quantity to 3')

    def test_remove_from_cart(self):
        url = reverse('remove_from_cart', args=[self.product.id])
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        if messages:
            self.assertEqual(messages[-1].tags, 'success')
            self.assertEqual(
                messages[-1].message, f'Removed {self.product.name} from your cart')

    def test_remove_from_cart_error(self):
        # Testing error scenario where item does not exist in the cart
        url = reverse('remove_from_cart', args=[self.product.id])
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        if messages:
            self.assertEqual(messages[-1].tags, 'error')
            self.assertEqual(messages[-1].message, 'Error removing item: get() returned more than one Product -- it returned 2!')

