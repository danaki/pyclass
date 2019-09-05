import pytest
from mysum import *

@pytest.fixture
def mysum_test_data():
    return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

def test_mysum_with_fixture(mysum_test_data):
    for data in mysum_test_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]

        assert mysum(num1, num2) == expected