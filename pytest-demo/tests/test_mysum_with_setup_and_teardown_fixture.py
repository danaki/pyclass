import pytest
from mysum import mysum

@pytest.fixture
def mysum_test_data():
    return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # setup part
    print('\nSetting up mock data')
    yield
    # teardown part
    print('\nCleaning after')

def test_mysum_with_setup_and_teardown_fixture(mysum_test_data):
    for num1, num2, expected in mysum_test_data:
        assert mysum(num1, num2) == expected