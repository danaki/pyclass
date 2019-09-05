import pytest
from mysum import *

@pytest.fixture(scope='module')
def mysum_test_data():
    print "Fixture is running"
    return [(3,5,8)]

def test_mysum_with_fixture(mysum_test_data):
    for num1, num2, expected in mysum_test_data:
        assert mysum(num1, num2) == expected

def test_mysum_with_fixture_2(mysum_test_data):
    for num1, num2, expected in mysum_test_data:
        assert mysum(num1, num2) == expected