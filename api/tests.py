from django.test import TestCase
from graphene.test import Client
from core.models import Product
from api.schema import schema


class ProductSchemaMutationTest(TestCase):
    def setUp(self):
        Product.objects.create(id=1, name="Buy milk")
        Product.objects.create(id=2, name="Pick up Tomatoes")

    @staticmethod
    def test_create_product():
        client = Client(schema)
        executed = client.execute('''mutation{createProduct(name: "Buy Soda"){success errors product{id name}}}''')
        assert executed['data']['createProduct']['success'] is True
        assert Product.objects.count() == 3

