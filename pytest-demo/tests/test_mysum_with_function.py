import pytest
from mysum import mysum

def test_mysum():
    assert mysum(1, 2) == 3

def test_mysum_output_type():
    assert type(mysum(1, 2)) is int