from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):

    def test_string_representation(self):
        product = Product(name="Buy eggs")
        self.assertEqual(str(product), product.name)
