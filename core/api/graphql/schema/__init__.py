import graphene

from core.api.graphql.schema.operation_query import Operation


class Query(Operation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
