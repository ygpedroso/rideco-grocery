import graphene
from api.graphql.query import Query
from api.graphql.mutation import Mutation


class RootQuery(Query, graphene.ObjectType):
    pass


class RootMutation(Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
