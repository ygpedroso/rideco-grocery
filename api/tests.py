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

    @staticmethod
    def test_create_product_with_missing_required_params():
        client = Client(schema)
        executed = client.execute('''mutation{createProduct(price: "Buy Soda"){success errors product{id name}}}''')
        assert len(executed['errors']) > 0
        assert Product.objects.count() == 2

    @staticmethod
    def test_remove_product():
        client = Client(schema)
        executed = client.execute('''mutation{removeProduct(productId: 1){success errors product{id name}}}''')
        assert executed['data']['removeProduct']['success'] is True
        assert Product.objects.count() == 1

    @staticmethod
    def test_remove_plan_with_missing_required_params():
        client = Client(schema)
        executed = client.execute('''mutation{removeProduct(id: 1){success errors product{id name}}}''')
        assert len(executed['errors']) > 0
        assert Product.objects.count() == 2
