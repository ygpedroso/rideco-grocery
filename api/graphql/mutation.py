import graphene
from core.models import Product
from api.graphql.types import ProductType


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        product = Product(name=name)
        product.save()

        return CreateProduct(product=product)


class RemoveProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        product_id = graphene.ID(required=True)

    def mutate(self, info, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return RemoveProduct(product=product)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    remove_product = RemoveProduct.Field()
