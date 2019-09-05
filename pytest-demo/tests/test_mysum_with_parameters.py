import pytest
from mysum import mysum

@pytest.mark.parametrize('num1, num2, expected', [(3,5,8)])
def test_mysum_with_one_value(num1, num2, expected):
        assert mysum(num1, num2) == expected

@pytest.mark.parametrize('num1, num2, expected',[(3,5,8),(-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)])
def test_mysum_with_multi_value(num1, num2, expected):
        assert mysum(num1, num2) == expected