import pytest
from mysum import mysum

class TestMySum(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_sum_example_with_class(self):
        assert mysum(1, 2) == 3

    @classmethod
    def teardown_class(cls):
        pass