import pytest

from bithacks import bithacks

def test_computeSign():
    assert(bithacks.computeSign(-42) == -1)
    assert(bithacks.computeSign(0) == 0)
    assert(bithacks.computeSign(42) == 1)

def test_detectOppositeSigns():
    assert(bithacks.detectOppositeSigns(-1,-1) == False)
    assert(bithacks.detectOppositeSigns(-1,1) == True)
    assert(bithacks.detectOppositeSigns(1,-1) == True)
    assert(bithacks.detectOppositeSigns(1,1) == False)
