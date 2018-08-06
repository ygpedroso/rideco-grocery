from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):

    def test_string_representation(self):
        product = Product(name="Buy eggs")
        self.assertEqual(str(product), product.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Product._meta.verbose_name_plural), "products")

    def test_product_creation(self):
        product = Product.objects.create(name="Buy soup")
        self.assertTrue(isinstance(product, Product))
