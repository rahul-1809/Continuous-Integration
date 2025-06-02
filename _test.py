import pytest

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n ** 5

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    
def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    
def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
        