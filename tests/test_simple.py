import pytest


@pytest.mark.parametrize("input_value", [1, True, False, "hello"])
def test_success(input_value):
    assert input_value == input_value


@pytest.mark.parametrize("input_value", [1, True, False, "hello"])
def test_failure(input_value):
    assert input_value != input_value
