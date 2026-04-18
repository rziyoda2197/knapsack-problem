import pytest
from your_module import knapsack

@pytest.mark.parametrize("weights, values, capacity, expected", [
    ([1, 2, 4, 2, 5], [5, 3, 5, 3, 2], 10, 14),
    ([1, 3, 4, 5], [1, 4, 5, 7], 7, 9),
    ([1, 2, 3], [6, 10, 12], 5, 22),
    ([1], [6], 0, 0),
    ([], [], 10, 0),
    ([1, 2, 3], [6, 10, 12], 0, 0),
])
def test_knapsack(weights, values, capacity, expected):
    assert knapsack(weights, values, capacity) == expected
