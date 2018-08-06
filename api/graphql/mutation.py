import graphene
from core.models import Product
from api.graphql.types import ProductType


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        try:
            product = Product(name=name)
            product.save()
            return CreateProduct(success=True, product=product)
        except Exception as err:
            return CreateProduct(success=False, errors=['exception', str(err)])


class RemoveProduct(graphene.Mutation):
    product = graphene.Field(ProductType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        product_id = graphene.ID(required=True)

    def mutate(self, info, product_id):
        try:
            product = Product.objects.get(id=product_id)
            Product.objects.get(id=product_id).delete()
            return RemoveProduct(success=True, product=product)
        except Exception as err:
            return RemoveProduct(success=False, errors=['exception', str(err)])


class UpdateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        product_id = graphene.ID(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, product_id, name):
        try:
            product = Product.objects.get(id=product_id)
            product.name = name
            product.save()
            return UpdateProduct(success=True, product=product)
        except Exception as err:
            return UpdateProduct(success=False, errors=['exception', str(err)])


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    remove_product = RemoveProduct.Field()
    update_product = UpdateProduct.Field()
