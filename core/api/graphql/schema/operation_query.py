import graphene

from core.service.operation import get_coalesced_operations


class OperationFields(graphene.ObjectType):
    strategy = graphene.String()
    deductible = graphene.Int()
    stop_loss = graphene.Int()
    oop_max = graphene.Int()


class OperationFilters(graphene.InputObjectType):
    member_id = graphene.String(required=True)
    strategy = graphene.String(required=True)


class Operation(graphene.ObjectType):
    get_operations = graphene.NonNull(OperationFields, filters=OperationFilters())

    def resolve_get_operations(self, info, filters: OperationFilters):
        member_id: str = filters.member_id
        strategy: str = filters.strategy
        return get_coalesced_operations(member_id, strategy)
