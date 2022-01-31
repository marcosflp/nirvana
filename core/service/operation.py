from core.constants.Operation import OperationStrategy
from core.integrations.api import Api1Session, Api2Session, Api3Session


def get_average_from_operations(
    deductible_values: list[int], stop_loss_values: list[int], oop_max_values: list[int]
):
    deductible_avg = int(sum(deductible_values) / len(deductible_values))
    stop_loss_avg = int(sum(stop_loss_values) / len(stop_loss_values))
    oop_max_avg = int(sum(oop_max_values) / len(oop_max_values))

    return {
        "deductible": deductible_avg,
        "stop_loss": stop_loss_avg,
        "oop_max": oop_max_avg,
    }


def get_count_from_operations(
    deductible_values: list[int], stop_loss_values: list[int], oop_max_values: list[int]
):
    deductible_avg = len(deductible_values)
    stop_loss_avg = len(stop_loss_values)
    oop_max_avg = len(oop_max_values)

    return {
        "deductible": deductible_avg,
        "stop_loss": stop_loss_avg,
        "oop_max": oop_max_avg,
    }


def get_max_from_operations(
    deductible_values: list[int], stop_loss_values: list[int], oop_max_values: list[int]
):
    deductible_avg = max(deductible_values)
    stop_loss_avg = max(stop_loss_values)
    oop_max_avg = max(oop_max_values)

    return {
        "deductible": deductible_avg,
        "stop_loss": stop_loss_avg,
        "oop_max": oop_max_avg,
    }


def get_min_from_operations(
    deductible_values: list[int], stop_loss_values: list[int], oop_max_values: list[int]
):
    deductible_avg = min(deductible_values)
    stop_loss_avg = min(stop_loss_values)
    oop_max_avg = min(oop_max_values)

    return {
        "deductible": deductible_avg,
        "stop_loss": stop_loss_avg,
        "oop_max": oop_max_avg,
    }


def get_sum_from_operations(
    deductible_values: list[int], stop_loss_values: list[int], oop_max_values: list[int]
):
    deductible_avg = sum(deductible_values)
    stop_loss_avg = sum(stop_loss_values)
    oop_max_avg = sum(oop_max_values)

    return {
        "deductible": deductible_avg,
        "stop_loss": stop_loss_avg,
        "oop_max": oop_max_avg,
    }


def coalesce_operations(
    strategy: OperationStrategy().available_strategies,
    deductible_values: list[int],
    stop_loss_values: list[int],
    oop_max_values: list[int],
):
    if strategy == OperationStrategy.AVERAGE:
        operations_result = get_average_from_operations(
            deductible_values, stop_loss_values, oop_max_values
        )
        operations_result["strategy"] = OperationStrategy.AVERAGE
    elif strategy == OperationStrategy.COUNT:
        operations_result = get_count_from_operations(deductible_values, stop_loss_values, oop_max_values)
        operations_result["strategy"] = OperationStrategy.COUNT
    elif strategy == OperationStrategy.MAX:
        operations_result = get_max_from_operations(deductible_values, stop_loss_values, oop_max_values)
        operations_result["strategy"] = OperationStrategy.MAX
    elif strategy == OperationStrategy.MIN:
        operations_result = get_min_from_operations(deductible_values, stop_loss_values, oop_max_values)
        operations_result["strategy"] = OperationStrategy.MIN
    elif strategy == OperationStrategy.SUM:
        operations_result = get_sum_from_operations(deductible_values, stop_loss_values, oop_max_values)
        operations_result["strategy"] = OperationStrategy.SUM
    else:
        raise ValueError("Invalid strategy")

    return operations_result


def get_coalesced_operations(
    member_id: str, strategy: OperationStrategy().available_strategies
):
    api1 = Api1Session()
    api2 = Api2Session()
    api3 = Api3Session()

    response_data_api1 = api1.get(member_id=member_id)
    response_data_api2 = api2.get(member_id=member_id)
    response_data_api3 = api3.get(member_id=member_id)

    deductible_values = [
        response_data_api1["deductible"],
        response_data_api2["deductible"],
        response_data_api3["deductible"],
    ]
    stop_loss_values = [
        response_data_api1["stop_loss"],
        response_data_api2["stop_loss"],
        response_data_api3["stop_loss"],
    ]
    oop_max_values = [
        response_data_api1["oop_max"],
        response_data_api2["oop_max"],
        response_data_api3["oop_max"],
    ]

    coalesced_operations = coalesce_operations(
        strategy=strategy,
        deductible_values=deductible_values,
        stop_loss_values=stop_loss_values,
        oop_max_values=oop_max_values,
    )

    return coalesced_operations
