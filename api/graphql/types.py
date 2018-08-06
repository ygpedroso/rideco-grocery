from graphene_django.types import DjangoObjectType
from core.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
