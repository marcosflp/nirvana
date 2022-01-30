import pytest

from core.constants.Operation import OperationStrategy
from core.service.operation import get_average_from_operations, coalesce_operations, get_coalesced_operations

pytestmark = pytest.mark.usefixtures("db")


@pytest.fixture
def deductible_values():
    return [1000, 1200, 1000]


@pytest.fixture
def stop_loss_values():
    return [10000, 13000, 10000]


@pytest.fixture
def oop_max_values():
    return [5000, 6000, 6000]


def test_get_average_from_operations(deductible_values, stop_loss_values, oop_max_values):
    expected_value = {
        "deductible": int(sum(deductible_values) / len(deductible_values)),
        "stop_loss": int(sum(stop_loss_values) / len(stop_loss_values)),
        "oop_max": int(sum(oop_max_values) / len(oop_max_values))
    }

    operations_average = get_average_from_operations(deductible_values, stop_loss_values, oop_max_values)
    assert operations_average == expected_value


def test_coalesce_operations(mocker, deductible_values, stop_loss_values, oop_max_values):
    mock_get_average_from_operations = mocker.patch("core.service.operation.get_average_from_operations")
    mock_get_average_from_operations.return_value = {
        'deductible': 1066,
        'stop_loss': 11000,
        'oop_max': 5666
    }

    expected_value = {
        "strategy": OperationStrategy.AVERAGE,
        'deductible': 1066,
        'stop_loss': 11000,
        'oop_max': 5666
    }

    # Test average strategy

    strategy = OperationStrategy.AVERAGE
    coalesced_result = coalesce_operations(strategy, deductible_values, stop_loss_values, oop_max_values)
    assert coalesced_result == expected_value

    # Test wrong strategy

    strategy = "wrong strategy"
    with pytest.raises(ValueError):
        coalesce_operations(strategy, deductible_values, stop_loss_values, oop_max_values)


def test_get_coalesced_operations(mocker):
    member_id = "1"
    mock_api1_get = mocker.patch("core.integrations.api.Api1Session.get")
    mock_api2_get = mocker.patch("core.integrations.api.Api2Session.get")
    mock_api3_get = mocker.patch("core.integrations.api.Api3Session.get")
    mock_coalesce_operations = mocker.patch("core.service.operation.coalesce_operations")

    mock_api1_get.return_value = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}
    mock_api2_get.return_value = {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}
    mock_api3_get.return_value = {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}
    mock_coalesce_operations.return_value = {
      "strategy": OperationStrategy.AVERAGE,
      "deductible": 1066,
      "stop_loss": 11000,
      "oop_max": 5666
    }

    get_coalesced_operations(member_id="1", strategy=OperationStrategy.AVERAGE)

    # Test func mock calls

    mock_api1_get.assert_called_once_with(member_id=member_id)
    mock_api2_get.assert_called_once_with(member_id=member_id)
    mock_api3_get.assert_called_once_with(member_id=member_id)
    mock_coalesce_operations.assert_called_once_with(
        strategy=OperationStrategy.AVERAGE,
        deductible_values=[1000, 1200, 1000],
        stop_loss_values=[10000, 13000, 10000],
        oop_max_values=[5000, 6000, 6000],
    )
