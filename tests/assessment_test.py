import pytest
from programs import example

def test_endsPy():
    assert example.endsPy("ilovepy") == True
    assert example.endsPy("welovepy") == True
    assert example.endsPy("welovepyforreal") == False
    assert example.endsPy("pyiscool") == False
    assert example.endsPy("hurrayforpY") == True

def test_two():
    assert example.two(2, 4, '+') == 6
    assert example.two(7, 3, '-') == 4
    assert example.two(3, 1.5, '*') == 4.5
    assert example.two(-5, 2, '/') == -2.5

def test_four():
    assert example.four(32, 24) == 8
    assert example.four(18, 11) == 1
    assert example.four(10, 50) == 10
    # for some reason I don't get 1 when the numbers divide by themselves 
    