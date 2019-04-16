from tour import *
import pytest

def test_to_chess_notation_happy_path():
    assert to_chess_notation(0, 0) == 'a1'

def test_to_chess_notation_raises_error_out_of_board():
    with pytest.raises(IndexError):
        to_chess_notation(100, 100)

def test_from_chess_notation_happy_path():
    assert from_chess_notation('a1') == (0, 0)

def test_from_chess_notation_raises_error_out_of_board():
    with pytest.raises(ValueError):
        from_chess_notation('z9')

def test_chess_notation_to_list_happy_path():
    assert chess_notation_to_list('a1 b2') == [(0, 0), (1, 1)]

def test_chess_notation_to_list_raises_error_if_one_of_elements_out_of_board():
    with pytest.raises(ValueError):
        chess_notation_to_list('a1 z9')

@pytest.mark.xfail(raises=AttributeError)
def test_chess_notation_to_list_will_fix_later():
    chess_notation_to_list(None)

@pytest.mark.skip
def test_chess_notation_to_list_skip_for_now():
    chess_notation_to_list({})

def get_is_board_hit_test_data():
    return [
        (0, 0, True),
        (-1, 0, False),
        (8, 8, False)
    ]

@pytest.mark.parametrize('x, y, expected', get_is_board_hit_test_data())
def test_is_board_hit(x, y, expected):
    assert is_board_hit(x, y) == expected

@pytest.fixture
def get_is_valid_move_test_data():
    return [
        [(0, 0), (7, 7), False],
        [(0, 0), (2, 1), True],
        [(7, 7), (9, 8), False],
        [(7, 7), (5, 6), True],
    ]

def test_sum(get_is_valid_move_test_data):
    for data in get_is_valid_move_test_data:
        fr, to, expected = data
        assert is_valid_move(fr, to) == expected
