import graphene
from core.models import Product
from api.graphql.types import ProductType


class Query(object):
    products = graphene.List(ProductType)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()
